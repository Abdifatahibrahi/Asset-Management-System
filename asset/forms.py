from dataclasses import fields
from unicodedata import decimal
from django import forms
from .models import Furniture

class FurnitureForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)