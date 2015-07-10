from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class landingView(TemplateView):
    template_name = 'base/index.html'