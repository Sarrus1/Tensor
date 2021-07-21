from django.contrib import admin
from .models import SbAdmins, SbServers, SbProtests

admin.site.register(SbAdmins)
admin.site.register(SbServers)
admin.site.register(SbProtests)