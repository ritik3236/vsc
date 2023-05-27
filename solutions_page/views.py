from django.shortcuts import render
from django.views.generic import TemplateView
from home_page.views import HomePageView, txt_to_list
from home_page.models import *
from solutions_page.models import *

# Create your views here.


class SolutionsView(TemplateView):
    template_name = "solutions.html"

    def get(self, request, sem_id=1, sub_name="Hindi", *args, **kwargs):
        solutions_queryset = ''
        s_links_queryset = ''
        if Subject.objects.filter(
                course_name_id__c_name=kwargs["c_name"]).exists():
            sub_list = list(Subject.objects.get(
                course_name_id__c_name=kwargs["c_name"]).sub_names.split(", "))
            try:
                solutions_id = QuesPaper.objects.get(
                    course_name_id__c_name=kwargs["c_name"], semester=sem_id, sub_name=sub_name.lower()).solutions_id
                solutions_queryset = list(SolutionsMedia.objects.filter(solutions_id = solutions_id))
                s_links_queryset = list(SolutionsLink.objects.filter(s_link_id = solutions_id))
            except:
                solutions_queryset = ''
                s_links_queryset  = ''
        else:
            sub_list = txt_to_list("Sorry We Got No Subjects 😔")
        
        context = {
            "sem_id": sem_id,
            "sub_list": sub_list,
            "sub_name": sub_name,
            "c_name_1": kwargs["c_name"],
            "solutions_queryset": solutions_queryset,
            "s_links_queryset":s_links_queryset,
            "sem_list": HomePageView.sem_list,
            "course_list": HomePageView.course_list,
        }

        return render(request, self.template_name, context)
