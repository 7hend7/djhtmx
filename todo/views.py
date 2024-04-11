from django.shortcuts import render

from django.template import Context, Template
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import django.urls as urls
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import ProcessFormView, BaseCreateView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, BaseDetailView
from django.conf import settings
from .models import Todos

class HomeTodoView(ListView):
    template_name = "todo_home.html"
    model = Todos

    allow_empty = True

    # -get method execute before get_query_set() & get_context_data() and calling their
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # -
        queryset = super().get_queryset()

        return queryset




