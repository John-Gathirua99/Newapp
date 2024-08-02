from django import forms

from .models import TodoList

from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.Form):

    class Meta:
        model = TodoList
        fields = ['activity','done','author',]