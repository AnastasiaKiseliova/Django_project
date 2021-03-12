from django.forms import ModelForm
from .models import Company, Project, Address, Phone, Email, Message, UserPhoto, Keyword
from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404
from .forms import CompanyForm, ProjectForm, AddressForm, PhoneForm, EmailForm, MessageForm, KeywordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class Index(generic.TemplateView):
    template_name = 'index.html'


class AccountView(generic.TemplateView):
    model = User
    template_name = 'CRM/personal-account.html'


class MessageView(generic.ListView):
    model = Message
    template_name = 'CRM/messages.html'
    paginate_by = 6

    def get_queryset(self):
        return Message.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Messages'] = self.get_queryset()
        return context


""" Views describing company """


class CompanyListNUView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_name_u.html"
    paginate_by = 10
    ordering = "title"

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListNUView, self).get_context_data(**kwargs)
        context['Companies_Title_Upright'] = self.object_list.order_by('title')
        return context


class CompanyListNRView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_name_r.html"
    paginate_by = 10
    ordering = "-title"

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListNRView, self).get_context_data(**kwargs)
        context['Companies_Title_Reversed'] = self.object_list.order_by('-title')
        return context


class CompanyListDUView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_date_u.html"
    paginate_by = 10
    ordering = "creation_date"

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListDUView, self).get_context_data(**kwargs)
        context['Companies_Date_Upright'] = self.object_list.order_by('creation_date')
        return context


class CompanyListDRView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_date_r.html"
    paginate_by = 10
    ordering = "-creation_date"

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListDRView, self).get_context_data(**kwargs)
        context['Companies_Date_Reversed'] = self.object_list.order_by('-creation_date')
        return context


class CompanyDetailView(generic.DetailView):
    model = Company

    def company_detail_view(request, primary_key):
        try:
            company = Company.objects.get(pk=primary_key)
            address = company.address_set.all()
        except Company.DoesNotExist:
            raise Http404('Company does not exist')

        return render(request, 'CRM/company_detail.html',
                      context={'company': company,
                               'address': address})


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            Company.objects.create(**form.cleaned_data)
            return redirect('companies-du')
    else:
        form = CompanyForm()
    return render(request, 'CRM/add_company.html', context={'form': form})


""" Views describing project """


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 3

    def get_queryset(self):
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['Projects'] = self.get_queryset()
        return context


class ProjectDetailView(generic.DetailView):
    model = Project

    def project_detail_view(request, primary_key):
        try:
            project = Project.objects.get(pk=primary_key)
        except Project.DoesNotExist:
            raise Http404('Project does not exist')

        return render(request, 'CRM/project_detail.html', context={'project': project})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            Project.objects.create(**form.cleaned_data)
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'CRM/add_project.html', context={'form': form})


def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            Address.objects.create(**form.cleaned_data)
            return redirect('companies-du')
    else:
        form = AddressForm()
    return render(request, 'CRM/add_address.html', context={'form': form})


def add_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            Phone.objects.create(**form.cleaned_data)
            return redirect('companies-du')
    else:
        form = PhoneForm()
    return render(request, 'CRM/add_phone.html', context={'form': form})


def add_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            Email.objects.create(**form.cleaned_data)
            return redirect('companies-du')
    else:
        form = EmailForm()
    return render(request, 'CRM/add_email.html', context={'form': form})


def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            author = request.user
            Message.objects.create(author=author, **form.cleaned_data)
            return redirect('messages')
    else:
        form = MessageForm()
    return render(request, 'CRM/add_message.html', context={'form': form})


def add_keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            Keyword.objects.create(name=form.cleaned_data['name'])
            return redirect('messages')
    else:
        form = KeywordForm()
    return render(request, 'CRM/add_keyword.html', context={'form': form})
