from django import forms
from django.forms import ModelForm
from .models import commet


class CommetForm(ModelForm):
    class Meta:
        model = commet
        fields = '__all__'

