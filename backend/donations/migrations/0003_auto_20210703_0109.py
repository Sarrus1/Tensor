# Generated by Django 3.0.5 on 2021-07-02 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20210703_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donators',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
