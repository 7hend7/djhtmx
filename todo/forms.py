
from django import forms
import django.urls as urls
from django.core.exceptions import ValidationError

from .models import Todos

from django.utils.dateparse import parse_date


class TodoCreateUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=512, required=True, widget=forms.Textarea( attrs={'placeholder': 'Enter todo please', 'class': 'form-control'} ))
    completed = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(attrs={"hidden":"true"}), label='')
    expired = forms.DateField(required=False,  widget=forms.widgets.Input({'type':'date'}), )

    # def clean_expired(self):
    #     expired = self.cleaned_data['expired']
          # do something... 
    #     return expired

    class Meta:
        model = Todos
        fields = ['name', 'expired', "completed"]


