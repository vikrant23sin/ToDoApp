from django import forms
from myapp.models import *

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'