# Generated by Django 5.0.7 on 2024-08-14 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_managernotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managernotification',
            old_name='manager',
            new_name='company',
        ),
    ]
