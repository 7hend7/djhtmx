
from django import forms
import django.urls as urls
from django.core.exceptions import ValidationError

from .models import Todos


class TodoCreateUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=512, required=True, widget=forms.Textarea( attrs={'placeholder': 'Enter todo please', 'class': 'form-control'} ))
    completed = forms.BooleanField(required=False)
    expired = forms.DateField(required=False, widget=forms.SelectDateWidget(attrs={}))  # input_formats=['%dd.%mm.%YYYY'] 

    class Meta:
        model = Todos
        fields = ['name', 'completed', 'expired']


