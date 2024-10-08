# Generated by Django 5.0.7 on 2024-08-11 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_alter_roledetail_company'),
        ('student', '0012_rename_studentinternship_studentappliedinternship'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentappliedinternship',
            options={'verbose_name_plural': 'Student Applied Internships'},
        ),
        migrations.CreateModel(
            name='StudentInternship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=12)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_internships', to='manager.roledetail')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'verbose_name_plural': 'Student Internships',
            },
        ),
    ]
