# Generated by Django 5.0.7 on 2024-07-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_studentrolesapplied_applicatondate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentrolesapplied',
            old_name='applicatonDate',
            new_name='applicationDate',
        ),
    ]
