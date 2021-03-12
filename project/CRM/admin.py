from django.contrib import admin
from .models import Project, Company, Message, Address, Phone, Email, UserPhoto, Keyword


admin.site.register(Message)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)


class ProjectInstanceInline(admin.TabularInline):
    model = Project
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'CEO')
    inlines = [ProjectInstanceInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'started')
    list_filter = ('started',)


@admin.register(UserPhoto)
class UserPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', )
