from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Project(models.Model):
    """ Model describing the project """

    name = models.CharField(max_length=30, default='None')
    description = models.TextField(max_length=250, null=True)
    started = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    finished = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='company')

    class Meta:
        ordering = ["-started"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.pk)])


class Company(models.Model):
    """ Model describing the company """

    title = models.CharField(max_length=30, default='None')
    description = models.TextField(max_length=500, null=True)
    CEO = models.CharField(max_length=30, default='Not Defined')
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return "/company/%i/" % self.pk


class Message(models.Model):
    """ Model describing the message """

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    text = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='project')

    TYPE = (
        ('a', 'application'),
        ('m', 'mail'),
        ('s', 'site'),
        ('i', 'initiative'),
    )

    interaction_type = models.CharField(max_length=1, choices=TYPE)

    VALUE = (
        ('l', 'like'),
        ('d', 'dislike'),
    )

    mark = models.CharField(max_length=1, choices=VALUE)

    def __str__(self):
        return self.text


class Address(models.Model):
    """ Model describing the address """
    address = models.CharField(max_length=100, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='address')

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address


class Phone(models.Model):
    """ Model describing the phone """
    phone = models.CharField(max_length=13, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='phone')

    def __str__(self):
        return self.phone


class Email(models.Model):
    """ Model describing the e-mail """
    email = models.EmailField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='email')

    def __str__(self):
        return self.email
