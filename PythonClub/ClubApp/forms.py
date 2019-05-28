from django import forms
from .models import Meeting, MeetingMinute, Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'