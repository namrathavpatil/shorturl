from django import forms
from django.core import validators


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your_name', max_length=100)


class urlForm(forms.Form):
    your_url = forms.CharField(label='Your_name', max_length=100)
