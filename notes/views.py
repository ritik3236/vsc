from django.shortcuts import render
from django.views.generic import TemplateView
from home_page.views import HomePageView, txt_to_list
from home_page.models import *
from notes.models import *

# Create your views here.


class NotesView(TemplateView):
    template_name = "notes.html"

    def get(self, request, sem_id=1, sub_name="Hindi", *args, **kwargs):
        notes_queryset = ''
        n_links_queryset = ''
        if Subject.objects.filter(
                course_name_id__c_name=kwargs["c_name"]).exists():
            sub_list = list(Subject.objects.get(
                course_name_id__c_name=kwargs["c_name"]).sub_names.split(", "))
            try:
                notes_id = QuesPaper.objects.get(
                    course_name_id__c_name=kwargs["c_name"], semester=sem_id, sub_name=sub_name.lower()).notes_id
                notes_queryset = list(NotesMedia.objects.filter(notes_id = notes_id))
                n_links_queryset = list(NotesLink.objects.filter(n_link_id = notes_id))
            except:
                notes_queryset = ''
                n_links_queryset = ''
        else:
            sub_list = txt_to_list("Sorry We Got No Subjects 😔")

        context = {
            "sem_id": sem_id,
            "sub_list": sub_list,
            "sub_name": sub_name,
            "c_name_1": kwargs["c_name"],
            "notes_queryset": notes_queryset,
            "n_links_queryset" : n_links_queryset,
            "sem_list": HomePageView.sem_list,
            "course_list": HomePageView.course_list,
        }

        return render(request, self.template_name, context)
