# Generated by Django 3.0.5 on 2021-07-02 23:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donators',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 23, 8, 41, 838476, tzinfo=utc)),
        ),
    ]
