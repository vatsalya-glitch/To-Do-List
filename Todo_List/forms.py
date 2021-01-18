from django import forms
from .models import Task

class Create_new_task(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ['date']