# Generated by Django 5.0.7 on 2024-08-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_alter_manager_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerProfileChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('ceo', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('durationOfExistence', models.CharField(max_length=100)),
                ('briefInfo', models.TextField()),
                ('companyLogo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
