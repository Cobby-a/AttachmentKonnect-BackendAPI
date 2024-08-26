# Generated by Django 5.0.7 on 2024-08-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_studentassessment_company_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentassessment',
            old_name='student_name',
            new_name='student_last_name',
        ),
        migrations.AddField(
            model_name='studentassessment',
            name='student_other_names',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
