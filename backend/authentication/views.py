from django.contrib.auth import logout
from django.shortcuts import render, redirect

from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth:index')

def LoginView(request):
    return render(request, 'authentication/login.html')
