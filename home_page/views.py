from django.shortcuts import render
from django.views.generic import TemplateView

from home_page.models import *

def error_404_view(request, exception):
    return render(request, "404.html",)

def sort_by_values(dic=None):
    if dic:
        return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}


def txt_to_list(txt, spacer=" "):
    return txt.split(spacer)


class HomePageView(TemplateView):
    template_name = "home_page.html"
    try:
        course_list = list(Course.objects.order_by("c_name").values_list("id", "c_name"))
    except Exception as e:
        print (e)
    sem_list = {
        "1": "1st",
        "2": "2nd",
        "3": "3rd",
        "4": "4th",
        "5": "5th",
        "6": "6th",
    }

    def get(self, request, *arg, **kwargs):

        context = {
            "course_list": self.course_list,
            "sem_list": self.sem_list,
            "sub_list": txt_to_list("Plz select Course & semester 👈"),
            "questions": ["Plz Select Any Subject 📚 "],
        }
        return render(request, self.template_name, context)


class QuestionView(HomePageView, TemplateView):
    template_name = "home_page.html"

    def get(self, request, sem_id=1, sub_name="Hindi", *args, **kwargs):
        questions = []
        ques_list = []
        sub_list =[]

        if Subject.objects.filter(course_name_id__c_name=kwargs["c_name"]).exists():
            sub_list = list(Subject.objects.get(course_name_id__c_name=kwargs["c_name"]).sub_names.split(", "))
            try:
                ques_list = QuesPaper.objects.get(
                    course_name_id__c_name=kwargs["c_name"],
                    semester=sem_id,
                    sub_name=sub_name.lower(),
                ).fl_id.split(",")
            except:
                ques_list = []
            for item in ques_list:
                try:
                    q_paper = QuesPaperMedia.objects.get(fl_id=item.lower())
                    questions.append(q_paper)
                except QuesPaperMedia.DoesNotExist:
                    q_paper = "None"
        else:
            sub_list = txt_to_list("Sorry We Got No Subjects 😔")

        if not questions:
            questions = ["Question Paper Missing"]
        context = {
            "sem_id": sem_id,
            "sub_list": sub_list,
            "sub_name": sub_name,
            "questions": questions,
            "c_name_1": kwargs["c_name"],
            "sem_list": HomePageView.sem_list,
            "course_list": HomePageView.course_list,
        }

        return render(request, self.template_name, context)
