# Generated by Django 5.0.7 on 2024-08-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_studentassessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassessment',
            name='suggestionsForImprovement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
