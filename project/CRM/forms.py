from django import forms
from .models import Company, Project, Address, Phone, Email, Message
from django.contrib.auth.models import User


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
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    company = forms.ModelChoiceField(Company.objects.all(), empty_label='Company',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class AddressForm(forms.Form):
    address = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.ModelChoiceField(Company.objects.all(), empty_label='Company',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.ModelChoiceField(Company.objects.all(), empty_label='Company',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class EmailForm(forms.Form):
    email = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.ModelChoiceField(Company.objects.all(), empty_label='Company',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    interaction_type = forms.ChoiceField(choices=Message.TYPE, widget=forms.Select(attrs={"class": "form-control"}))
    mark = forms.ChoiceField(choices=Message.VALUE, widget=forms.Select(attrs={"class": "form-control"}))
    project = forms.ModelChoiceField(Project.objects.all(), empty_label='Project',
                                     widget=forms.Select(attrs={"class": "form-control"}))
    author = 0


class KeywordForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
