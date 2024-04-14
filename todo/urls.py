
from django.urls import re_path, path
from . import views


urlpatterns = [
    path("", views.ListTodoView.as_view(), name='list_todo'),
    path("delete/<int:id>", views.delete_todo, name='delete_todo'),

]