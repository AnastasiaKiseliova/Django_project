# Generated by Django 3.1.6 on 2021-03-04 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0007_auto_20210303_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CRM.project', verbose_name='project'),
            preserve_default=False,
        ),
    ]
