# Generated by Django 5.0.7 on 2024-08-22 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0004_supervisornotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisornotification',
            name='supervisor',
        ),
    ]
