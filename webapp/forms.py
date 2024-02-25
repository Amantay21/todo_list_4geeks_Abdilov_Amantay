from django import forms
from webapp.models import Task


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')

