# Generated by Django 3.0.8 on 2020-10-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamuser',
            name='can_control',
            field=models.BooleanField(default=False),
        ),
    ]
