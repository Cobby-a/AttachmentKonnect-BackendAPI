# Generated by Django 5.0.7 on 2024-08-01 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_alter_roledetail_company'),
        ('student', '0009_rename_applicatondate_studentrolesapplied_applicationdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInternship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=12)),
                ('smallInfo', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_data', models.DateField(blank=True, null=True)),
                ('optionalFile', models.DateField(auto_now_add=True, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_accepted_roles', to='manager.roledetail')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'verbose_name_plural': 'Student Internships',
            },
        ),
        migrations.DeleteModel(
            name='StudentAcceptedRoles',
        ),
    ]
