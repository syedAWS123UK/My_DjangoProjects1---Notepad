# forms.py
from django import forms
from .models import TextFile

class TextFileForm(forms.ModelForm):
    class Meta:
        model = TextFile
        fields = ['notepad_app', 'content']