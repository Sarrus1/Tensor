from .models import SbBans
from rest_framework import serializers

class BansSerializer(serializers.HyperlinkedModelSerializer):

	bid = serializers.PrimaryKeyRelatedField(read_only=True)
	admin_name = serializers.ReadOnlyField()
	duration = serializers.ReadOnlyField()
	date_start = serializers.ReadOnlyField()
	date_end = serializers.ReadOnlyField()
	percent = serializers.ReadOnlyField()
	authid = serializers.ReadOnlyField()
	steam64 = serializers.ReadOnlyField()
	steam3 = serializers.ReadOnlyField()
	ban_length = serializers.ReadOnlyField()
	sid = serializers.StringRelatedField()
	totalBans = serializers.ReadOnlyField()
	blocked = serializers.StringRelatedField(many=True)

	class Meta:
		model = SbBans
		exclude = ['ip']