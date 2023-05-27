from django.views.generic import TemplateView
from django.shortcuts import render


from about.models import *
from about.forms import *


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return(render(request, self.template_name))
