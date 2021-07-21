# Generated by Django 3.0.8 on 2020-11-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Server', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Discord', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Experience', models.CharField(max_length=100)),
                ('Experience_more', models.TextField()),
                ('Reason', models.TextField()),
                ('SteamID', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(default='Pending', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Moderator Applications',
            },
        ),
    ]
