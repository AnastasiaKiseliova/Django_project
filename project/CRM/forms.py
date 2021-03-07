from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Company, Project, Address, Phone, Email


class CompanyForm(forms.Form):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    CEO = forms.CharField(max_length=30, label='CEO', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    address = forms.ModelChoiceField(Address.objects.all(), empty_label='str. 00-00 City Country',
                                     widget=forms.Select(attrs={"class": "form-control"}))
    phone = forms.ModelChoiceField(Phone.objects.all(), empty_label='+380(--) --- -- --',
                                     widget=forms.Select(attrs={"class": "form-control"}))
    email = forms.ModelChoiceField(Email.objects.all(), empty_label='my_mail@mail.com',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField()
    company = forms.ModelChoiceField(Company.objects.all(), empty_label='Company')
