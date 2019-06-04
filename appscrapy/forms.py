from django import forms
from .models import *
from django.core.exceptions import ValidationError


class SiteForm(forms.Form):
    name = forms.CharField(max_length=150)
    start_url = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)

    def clean_data(self):
        new_name = self.cleaned_data['name'].lower()
        if new_name == 'create':
           raise ValidationError('Name may not be "create"')

        return new_name

    def save(self):
        new_site = Site.objects.create(
            name = self.cleaned_data['name'],
            start_url = self.cleaned_data['start_url'],
            description = self.cleaned_data['description'],
            )
        return new_site

#class JobForm(forms.Form):
