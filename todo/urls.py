
from django.urls import re_path, path
from . import views


urlpatterns = [
    path("", views.HomeTodoView.as_view(), name='home_todo')    
]