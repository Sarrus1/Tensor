from .models import SbBans
from rest_framework import serializers

class BansSerializer(serializers.ModelSerializer):

	bid = serializers.PrimaryKeyRelatedField(read_only=True)
	admin_name = serializers.ReadOnlyField()
	duration = serializers.ReadOnlyField()
	date_start = serializers.ReadOnlyField()
	date_end = serializers.ReadOnlyField()
	percent = serializers.ReadOnlyField()
	steam64 = serializers.ReadOnlyField()
	steam3 = serializers.ReadOnlyField()
	ban_length = serializers.ReadOnlyField()
	totalBans = serializers.ReadOnlyField()
	bannedFrom = serializers.ReadOnlyField()
	blocked = serializers.StringRelatedField(many=True, required=False)


	class Meta:
		model = SbBans
		exclude = ['ip']