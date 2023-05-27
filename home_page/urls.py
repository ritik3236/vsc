from django.urls import path
from home_page.views import *

app_name = 'home_page'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('Q_paper/', QuestionView.as_view(), name='ques'),
    path('Q_paper/<str:c_name>/', QuestionView.as_view(), name='ques'),
    path('Q_paper/<str:c_name>/<int:sem_id>/', QuestionView.as_view(), name='sem'),
    path('Q_paper/<str:c_name>/<int:sem_id>/<str:sub_name>', QuestionView.as_view(), name='subject'),
]
