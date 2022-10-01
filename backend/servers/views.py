from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from tensor_site.decorators import login_required_message
from django.contrib import messages
import paramiko
from os import getenv


class ServerView(TemplateView):
    template_name = 'servers/servers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            canControl = "true" if self.request.user.can_control else "false"
        else:
            canControl = "false"
        context["canControl"] = canControl
        return context


@login_required_message
@login_required
def ServersControlView(request, server_port, server_command):
    if not request.user.can_control:
        messages.success(
            request, "You don't have permission to do that.", extra_tags='danger')
        return HttpResponseRedirect("/servers/")
    else:
        if server_command == "1":
            server_command = "start"
        elif server_command == "2":
            server_command = "stop"
        elif server_command == "3":
            server_command = "restart"
        elif server_command == "4":
            server_command = "fu"
        server = Server.objects.get(port=server_port)
        hostname = "192.168.1.107"
        password = getenv("DB_AWP_PASS")
        username = server.user
        port = 12345
        command = "cd /home/"+server.user+" && ./" + \
            server.instance_name+" "+server_command
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            client.connect(hostname, port=port,
                           username=username, password=password)
            stdin, stdout, stderr = client.exec_command(command)
            out = stdout.read().decode().strip()
            if server_command == 'start':
                messages.success(request, 'Successfuly started ' +
                                 server.name, extra_tags='success')
            elif server_command == 'stop':
                messages.success(request, 'Successfuly stopped ' +
                                 server.name, extra_tags='success')
            elif server_command == 'restart':
                messages.success(request, 'Successfuly restarted ' +
                                 server.name, extra_tags='success')
            elif server_command == 'fu':
                messages.success(request, 'Successfuly updated ' +
                                 server.name, extra_tags='success')
        except:
            messages.success(request, 'An error has occured.',
                             extra_tags='danger')
        finally:
            client.close()
            return HttpResponseRedirect("/servers/")
