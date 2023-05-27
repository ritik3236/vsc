from django.urls import path
from notes.views import *

app_name = 'notes'
urlpatterns = [
    path('notes/', NotesView.as_view(), name='notes'),
    path('notes/<str:c_name>/', NotesView.as_view(), name='notes'),
    path('notes/<str:c_name>/<int:sem_id>/', NotesView.as_view(), name='notes'),
    path('notes/<str:c_name>/<int:sem_id>/<str:sub_name>', NotesView.as_view(), name='notes'),
]