# Generated by Django 3.2.3 on 2021-05-26 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_exchange_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='exchange_user',
        ),
    ]
