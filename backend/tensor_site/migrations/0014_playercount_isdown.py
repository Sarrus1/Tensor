# Generated by Django 3.0.5 on 2021-03-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tensor_site', '0013_playercount_current_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='playercount',
            name='isdown',
            field=models.BooleanField(default=False),
        ),
    ]
