# Generated by Django 3.0.5 on 2021-07-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestatistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankAwpSeason',
            fields=[
                ('steam', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('lastip', models.TextField(blank=True, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('kills', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('deaths', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('assists', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('suicides', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tk', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('shots', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hits', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('headshots', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('connected', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('rounds_tr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('rounds_ct', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('lastconnect', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('knife', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('glock', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hkp2000', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('usp_silencer', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p250', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('deagle', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('elite', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('fiveseven', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tec9', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('cz75a', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('revolver', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('nova', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('xm1014', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mag7', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sawedoff', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('bizon', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mac10', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp9', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp7', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ump45', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p90', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('galilar', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ak47', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('scar20', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('famas', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m4a1', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m4a1_silencer', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aug', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ssg08', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sg556', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('awp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('g3sg1', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m249', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('negev', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hegrenade', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('flashbang', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('smokegrenade', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('inferno', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('decoy', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('taser', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp5sd', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('breachcharge', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('head', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('chest', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('stomach', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('left_arm', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('right_arm', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('left_leg', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('right_leg', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_planted', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_exploded', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_defused', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ct_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tr_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hostages_rescued', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_killed', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_escaped', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_played', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mvp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('damage', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_draw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_lose', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('first_blood', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('no_scope', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('no_scope_dis', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'rankme_season',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RankAwpSeasonId',
            fields=[
                ('season_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rankme_season_id',
                'abstract': False,
                'managed': False,
            },
        ),
    ]
