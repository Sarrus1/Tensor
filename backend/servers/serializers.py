from .models import Server, PlayerCount
from rest_framework import serializers


class ServersSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
			model = Server
			fields = ['name', 'ip', 'port']


class PlayerCountSerializer(serializers.HyperlinkedModelSerializer):
		server = ServersSerializer(read_only=True)
		class Meta:
			model = PlayerCount
			fields = ['server', 'timestamp', 'player_count', 'max_player', 'current_map']