# Generated by Django 5.0.7 on 2024-07-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_manager_companylogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='companyLogo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
