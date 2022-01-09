from django import forms
from .models import Task, Finish


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class FinishForm(forms.ModelForm):
    class Meta:
        model = Finish
        fields = "__all__"
