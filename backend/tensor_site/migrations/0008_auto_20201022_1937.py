# Generated by Django 3.0.8 on 2020-10-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tensor_site', '0007_applicationmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
