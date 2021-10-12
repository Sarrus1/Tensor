from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tensor_site.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('markdownx/', include('markdownx.urls')),
    path('', include(('authentication.urls', 'authentication'), namespace='auth')),
    path('', include('servers.urls')),
    path('', include('adminform.urls')),
    path('', include('sourcebans.urls')),
    path('', include('donations.urls')),
    path('', include('gamestatistics.urls')),
    path('polls/', include('polls.urls')),
    path('api/bans/', include('sourcebans.api_urls')),
    path('api/steamuserinfo/', include('authentication.api_urls')),
    path('api/servers/', include('servers.api_urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
