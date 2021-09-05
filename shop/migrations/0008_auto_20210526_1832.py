# Generated by Django 3.2.3 on 2021-05-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_bid_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='sold',
        ),
        migrations.AddField(
            model_name='auction',
            name='sold',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
