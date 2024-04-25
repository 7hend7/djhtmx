from typing import Any
from django.shortcuts import render

from django.template import Context, Template
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

import django.urls as urls
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect

from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import ProcessFormView, BaseCreateView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, BaseDetailView
from django.conf import settings
from django.views.generic import CreateView


from django.core.paginator import Paginator

from http import HTTPStatus

from .models import Todos
from .forms import TodoCreateUpdateForm


# consts
TODO_LISTVIEW_PAGINATE_BY = 5


class ListTodoView(ListView):
    template_name = "todo_list.html"
    model = Todos

    paginate_by = TODO_LISTVIEW_PAGINATE_BY

    # our context variable name
    context_object_name = 'todo_list'
    # allow empty list 'todo_list' 
    allow_empty = True

    # -get method execute before get_query_set() & get_context_data() and calling their
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # -
        queryset = super().get_queryset()

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        return super().get_context_data(**kwargs)


# return an instance of this class to redirect the client
class HttpResponseHtmxRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['HX-Redirect'] = self['Location']
    status_code = 200


@require_http_methods(['DELETE'])
def delete_todo(request, id):

    todo = get_object_or_404(Todos, id=id)

    
    # if request.method == "DELETE":
    try:
        todo.delete()
    except Exception as e:
        error_message = "delete error is: " + str(e)
        return HttpResponse(error_message)


    # todos = Todos.objects.all()
    # return render(request, "todo_list.html", {'todo_list':todos})

    # for redirect to another page
    response = HttpResponseHtmxRedirect(reverse("list_todo"))
    return response

    # return HttpResponse("Todo was deleted")
    # return redirect(reverse("todo:list_todo"))


# class TodoCreateView(CreateView):
#     model = Todos
#     template_name = 'product/todo_add.html'
#     form_class = TodoCreateUpdateForm

@require_http_methods(['GET', 'POST'])
def add_todo(request):
    if request.method == "POST":
        form = TodoCreateUpdateForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(f"-> form is valid: {form.cleaned_data}")
            form.save()
            return HttpResponseRedirect(reverse('list_todo'))
    else:
        # create empty form for sending it to client
        form = TodoCreateUpdateForm()
    return render(request, "todo_add.html", {'form': form})


@require_http_methods(['GET', 'POST'])
def detail_todo(request, id):
    obj = get_object_or_404(Todos, id=id)
    print(f" get object: {obj}")
    return render(request, "_todo_detail.html", {'item': obj})

# from django.utils.dateparse import parse_date


@require_http_methods(['POST'])
def update_todo(request, id):

    data = {}
    obj = get_object_or_404(Todos, id=id)

    data["name"] = request.POST.get("name", obj.name)
    data["completed"] = request.POST.get("completed", obj.completed)
    data["expired"] = request.POST.get("expired", obj.expired)

    print(f"-> completed contain:{request.POST.__contains__("completed")} / {request.POST.get("completed")}")
    print(f"-> data is {data}")

    form = TodoCreateUpdateForm(data=data, instance=obj)  # request.POST or None 
    if form.is_valid():
        print(f"-> form is valid \n cleaned_data: {form.cleaned_data}")
        form.save()
        return HttpResponse('Ok', HTTPStatus.OK)
    else:
        print(f"-> form is invalid \n  cleaned_data: {form.cleaned_data}")
        return HttpResponse('!', HTTPStatus.BAD_REQUEST)

# MyTable.objects.filter(pk=some_value).update(field1='some value')
