from django.forms import ModelForm
from .models import Company, Project, Address, Message
from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .forms import CompanyForm
from django.contrib.auth.models import User


class Index(generic.TemplateView):
    template_name = 'index.html'
    model = Company


class AccountView(generic.TemplateView):
    model = User
    template_name = 'CRM/personal-account.html'


class MessageView(generic.ListView):
    model = Message
    template_name = 'CRM/messages.html'

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
    paginate_by = 6

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListNUView, self).get_context_data(**kwargs)
        context['Companies'] = self.get_queryset()
        context['Companies_Title_Upright'] = self.object_list.order_by('title')
        return context


class CompanyListNRView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_name_r.html"
    paginate_by = 6

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListNRView, self).get_context_data(**kwargs)
        context['Companies'] = self.get_queryset()
        context['Companies_Title_Reversed'] = self.object_list.order_by('-title')
        return context


class CompanyListDUView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_date_u.html"
    paginate_by = 6

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListDUView, self).get_context_data(**kwargs)
        context['Companies'] = self.get_queryset()
        context['Companies_Date_Upright'] = self.object_list.order_by('creation_date')
        return context


class CompanyListDRView(generic.ListView):
    model = Company
    template_name = "CRM/companies_by_date_r.html"
    paginate_by = 6

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyListDRView, self).get_context_data(**kwargs)
        context['Companies'] = self.get_queryset()
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
    form = 0

    if request.method == 'POST':
        pass
    else:
        form = CompanyForm()
    return render(request, 'CRM/add_company.html', context={'form': form})


""" Views describing project """


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 8

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


class AddProject():
    pass
