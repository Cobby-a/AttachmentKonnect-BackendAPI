# Generated by Django 5.0.7 on 2024-08-11 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_alter_roledetail_company'),
        ('student', '0011_alter_studentinternship_optionalfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentInternship',
            new_name='StudentAppliedInternship',
        ),
    ]
