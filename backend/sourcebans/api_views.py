from enum import Enum
from django.db.models import Q
from rest_framework import filters, permissions, pagination, viewsets
from rest_framework.throttling import UserRateThrottle
from django.http import HttpResponse
from django.utils.timezone import localtime
from time import mktime
import django_filters
from .permissions import sbPermissions

from .serializers import BansSerializer

from .models import *
from .filter import *
from .tables import *


class requestTypeEnum(Enum):
		delete = 1
		update = 2

class DefaultResultsSetPagination(pagination.PageNumberPagination):
		page_size = 10
		page_size_query_param = 'limit'
		max_page_size = 100

class BansFilter(django_filters.FilterSet):
		search = django_filters.CharFilter(method='search_filter', label="search")
		bid = django_filters.NumberFilter(field_name="bid", lookup_expr="iexact", label="bid")

		def search_filter(self, queryset, name, value):
				return SbBans.objects.filter(
						Q(authid__icontains=value) | Q(name__icontains=value)
				)
		
		class Meta:
				model = SbBans
				fields = ["search", "bid"]

class BurstRateThrottle(UserRateThrottle):
		rate = '20/min'

class BansViewSet(viewsets.ModelViewSet):
		"""API endpoint for the bans list"""
		queryset = SbBans.objects.all().order_by('-bid')
		serializer_class = BansSerializer
		throttle_classes = [BurstRateThrottle]
		permission_classes = [permissions.IsAuthenticatedOrReadOnly]
		filter_backends = [filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
		ordering_fields = ['name', 'created']
		ordering = '-created'
		pagination_class = DefaultResultsSetPagination
		filterset_class = BansFilter

		def update(self, request, *args, **kwargs):
				requestUser = request.user
				instance = self.get_object()

				if(not requestUser.is_admin):
					return HttpResponse(status=403)
				if(not canAdminEditBan(instance.bid, requestUser.sb_admin_id)):
					return HttpResponse(status=403)

				update_type = request.data['update_type']
				aid = requestUser.sb_admin_id
				if update_type == requestTypeEnum.delete.value:
					instance.removedon = mktime(localtime())
					instance.removedby = aid
					instance.removetype = "E"
					instance.save()
					return HttpResponse(status=200)
				if update_type == requestTypeEnum.update.value:
					serializer = BansSerializer(instance=instance, data=request.data, partial=True)
					if serializer.is_valid():
						self.perform_update(serializer)
						return HttpResponse(status=200)
				return HttpResponse(status=500)
				
		def destroy(self, request, pk=None):
				requestUser = request.user
				bid=pk
				if(not requestUser.is_admin):
					return HttpResponse(status=403)
				if(not canAdminEditBan(bid, requestUser.sb_admin_id)):
					return HttpResponse(status=403)

				SbBans.objects.get(bid=bid).delete()
				return HttpResponse(status=200)


def canAdminEditBan(bid, aid):
		user = SbAdmins.objects.get(aid=aid)
		ban = SbBans.objects.get(bid=bid)
		userPermissions = user.gid.flags
		if(user.extraflags != 0):
			userPermissions = user.extraflags
		if(bool(sbPermissions["ADMIN_EDIT_ALL_BANS"]["value"] & userPermissions)):
			return True
		if(bool(sbPermissions["ADMIN_EDIT_OWN_BANS"]["value"] & userPermissions and ban.aid == aid)):
			return True
		if(bool(sbPermissions["ADMIN_EDIT_GROUP_BANS"]["value"] & userPermissions)):
			group = SbAdmins.objects.get(aid=ban.aid).gid
			return user.gid==group
		return False