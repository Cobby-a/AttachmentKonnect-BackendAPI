# Generated by Django 5.0.7 on 2024-07-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_roledetail_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='roledetail',
            name='moreInfo',
            field=models.TextField(null=True),
        ),
    ]
