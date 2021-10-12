from django.shortcuts import render
from django.views.generic.base import TemplateView


class PollColorsView(TemplateView):
    template_name = 'polls/poll-colors.html'
