
from django import forms
import django.urls as urls
from django.core.exceptions import ValidationError

from .models import Todos

from django.utils.dateparse import parse_date


class TodoCreateUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=512, required=True, widget=forms.Textarea( attrs={'placeholder': 'Enter todo please', 'class': 'form-control'} ))
    completed = forms.BooleanField(required=False)
    expired = forms.DateField(required=False,  widget=forms.SelectDateWidget(attrs={}))  # input_formats=['%dd.%mm.%YYYY'] 

    # def clean_expired(self):
    #     print("-> in clean form!")
    #     expired = self.cleaned_data['expired']
    #     print(f" type in clean form: {type(expired)}")
    #     return expired

    class Meta:
        model = Todos
        fields = ['name', 'completed', 'expired']


