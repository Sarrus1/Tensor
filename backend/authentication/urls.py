from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from authentication.views import IndexView, LogoutView, LoginView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^logout', login_required(LogoutView.as_view(), login_url='/'), name='logout'),
    path('login/', LoginView, name='login_page'),
]
