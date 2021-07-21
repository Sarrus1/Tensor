from rest_framework import viewsets, views, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import localtime
from .models import ServerControlModel
import paramiko
from .forms import ServerControlForm
import threading
from tensor_site.auth_tokens import *

class StandardResultsSetPagination(PageNumberPagination):
    page_size = Server.objects.all().count()
    page_size_query_param = 'page_size'
    max_page_size = Server.objects.all().count()


class ServersViewSet(viewsets.ModelViewSet):
		queryset = PlayerCount.objects.all().order_by('-id')
		serializer_class = PlayerCountSerializer
		http_method_names = ['get']
		pagination_class = StandardResultsSetPagination


class PlayerCountView(views.APIView):

		def get(self, request, format=None, *args, **kwargs):
			serverData = []
			servers = Server.objects.all().order_by("id")
			for server in servers:
				labels = []
				number = []
				q = PlayerCount.objects.filter(server=server).order_by("id")
				for data in q:
						labels.append(localtime(data.timestamp).strftime("%H:%M"))
						number.append(data.player_count)
				currentInfo = q.last()
				serverInfo = {
						'serverName': server.name,
						'maxPlayer': currentInfo.max_player,
						'connectionInfo': server.connectionInfo,
						'currentMap': currentInfo.current_map,
						'currentPlayers': currentInfo.player_count,
						'labels': labels.copy(),
						'data': number.copy(),
						'port': server.port
				}
				serverData.append(serverInfo)
			return JsonResponse(serverData, safe=False)

def AsyncSSHCommand(body):
		command = body['command']
		uuid = body['uuid']
		port = body['port']

		if command=="1":
			command="start"
		elif command=="2":
			command="stop"
		elif command=="3":
			command="restart"
		elif command=="4":
			command="fu"
		
		server = Server.objects.get(port=port)
		hostname = "cs.tensor.fr"
		password = password_DB_awp
		username = server.user
		sshPort = server.sshport
		sshCommand = "cd /home/{} && ./{} {}".format(server.user, server.instance_name, command)
		
		serverControl = ServerControlModel(uuid=uuid, output="Sending command...").save()
		
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.WarningPolicy())
		client.connect(hostname, port=sshPort, username=username, password=password)
		stdin, stdout, stderr = client.exec_command(sshCommand, get_pty=True)
		while True:
			v = stdout.channel.recv(1024)
			if not v:
				break
			serverControl = ServerControlModel.objects.get(uuid=uuid)
			serverControl.output += "\n{}".format(v.decode("utf-8"))
			serverControl.save()
		client.close()
		server = ServerControlModel.objects.filter(uuid=uuid).order_by("-id").first()
		server.status = 1
		server.save()


class ServerControlView(views.APIView):
		permission_classes = [permissions.IsAuthenticated]
		form_class = ServerControlForm
		
		def post(self, request, *args, **kwargs):
				if not request.user.is_authenticated:
					return HttpResponse(status=403)
				if not request.user.can_control:
					return HttpResponse(status=403)
				proc = threading.Thread(target=AsyncSSHCommand, args=(request.data,))
				proc.start()
				return HttpResponse(status=200)
		
		def get(self, request, *args, **kwargs):
				if not request.user.is_authenticated:
					return HttpResponse(status=403)
				if not request.user.can_control:
					return HttpResponse(status=403)
				uuid = request.GET.get('uuid')
				controlStatus = ServerControlModel.objects.filter(uuid=uuid).order_by("-id").first()
				if(controlStatus is not None):
					output = controlStatus.output
					timestamp = controlStatus.timestamp
					if(controlStatus.status == 1):
						for server in ServerControlModel.objects.filter(uuid=uuid).order_by("-id"):
							server.delete()
					return JsonResponse({
						"timestamp": timestamp,
						"output": output,
					})
				else:
					return JsonResponse({
						"timestamp": "",
						"output": "NULL_RESPONSE"
					})
