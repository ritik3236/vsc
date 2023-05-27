from django.urls import path
from solutions_page.views import *

app_name = 'solutions_page'
urlpatterns = [
    path('solutions/', SolutionsView.as_view(), name='solutions'),
    path('solutions/<str:c_name>/', SolutionsView.as_view(), name='solutions'),
    path('solutions/<str:c_name>/<int:sem_id>/', SolutionsView.as_view(), name='solutions'),
    path('solutions/<str:c_name>/<int:sem_id>/<str:sub_name>', SolutionsView.as_view(), name='solutions'),
]