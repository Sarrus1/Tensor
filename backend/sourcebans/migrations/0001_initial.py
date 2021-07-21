# Generated by Django 3.0.5 on 2021-03-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SbAdmins',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=64, unique=True)),
                ('authid', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('gid', models.IntegerField()),
                ('email', models.CharField(max_length=128)),
                ('validate', models.CharField(blank=True, max_length=128, null=True)),
                ('extraflags', models.IntegerField()),
                ('immunity', models.IntegerField()),
                ('srv_group', models.CharField(blank=True, max_length=128, null=True)),
                ('srv_flags', models.CharField(blank=True, max_length=64, null=True)),
                ('srv_password', models.CharField(blank=True, max_length=128, null=True)),
                ('lastvisit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sb_admins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbAdminsServersGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('srv_group_id', models.IntegerField()),
                ('server_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_admins_servers_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbBanlog',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('bid', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_banlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbBans',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(blank=True, max_length=32, null=True)),
                ('authid', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('created', models.IntegerField()),
                ('ends', models.IntegerField()),
                ('length', models.IntegerField()),
                ('reason', models.TextField()),
                ('aid', models.IntegerField()),
                ('adminip', models.CharField(db_column='adminIp', max_length=32)),
                ('sid', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=4, null=True)),
                ('removedby', models.IntegerField(blank=True, db_column='RemovedBy', null=True)),
                ('removetype', models.CharField(blank=True, db_column='RemoveType', max_length=3, null=True)),
                ('removedon', models.IntegerField(blank=True, db_column='RemovedOn', null=True)),
                ('type', models.IntegerField()),
                ('ureason', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sb_bans',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbComments',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('bid', models.IntegerField()),
                ('type', models.CharField(max_length=1)),
                ('aid', models.IntegerField()),
                ('commenttxt', models.TextField()),
                ('added', models.IntegerField()),
                ('editaid', models.IntegerField(blank=True, null=True)),
                ('edittime', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sb_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbComms',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('authid', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('created', models.IntegerField()),
                ('ends', models.IntegerField()),
                ('length', models.IntegerField()),
                ('reason', models.TextField()),
                ('aid', models.IntegerField()),
                ('adminip', models.CharField(db_column='adminIp', max_length=32)),
                ('sid', models.IntegerField()),
                ('removedby', models.IntegerField(blank=True, db_column='RemovedBy', null=True)),
                ('removetype', models.CharField(blank=True, db_column='RemoveType', max_length=3, null=True)),
                ('removedon', models.IntegerField(blank=True, db_column='RemovedOn', null=True)),
                ('type', models.IntegerField()),
                ('ureason', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sb_comms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbDemos',
            fields=[
                ('demid', models.IntegerField(primary_key=True, serialize=False)),
                ('demtype', models.CharField(max_length=1)),
                ('filename', models.CharField(max_length=128)),
                ('origname', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'sb_demos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbGroups',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField()),
                ('name', models.CharField(max_length=128)),
                ('flags', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbLog',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=512)),
                ('message', models.TextField()),
                ('function', models.TextField()),
                ('query', models.TextField()),
                ('aid', models.IntegerField()),
                ('host', models.TextField()),
                ('created', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbMods',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('icon', models.CharField(max_length=128)),
                ('modfolder', models.CharField(max_length=64, unique=True)),
                ('steam_universe', models.IntegerField()),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_mods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbOverrides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=32)),
                ('flags', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sb_overrides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbProtests',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('bid', models.IntegerField()),
                ('datesubmitted', models.IntegerField()),
                ('reason', models.TextField()),
                ('email', models.CharField(max_length=128)),
                ('archiv', models.IntegerField(blank=True, null=True)),
                ('archivedby', models.IntegerField(blank=True, null=True)),
                ('pip', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'sb_protests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbServers',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=64)),
                ('port', models.IntegerField()),
                ('rcon', models.CharField(max_length=64)),
                ('modid', models.IntegerField()),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_servers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbServersGroups',
            fields=[
                ('server_id', models.IntegerField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sb_servers_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=128, unique=True)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'sb_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbSrvgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flags', models.CharField(max_length=30)),
                ('immunity', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=120)),
                ('groups_immune', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sb_srvgroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbSrvgroupsOverrides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.PositiveSmallIntegerField()),
                ('type', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=32)),
                ('access', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'sb_srvgroups_overrides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SbSubmissions',
            fields=[
                ('subid', models.AutoField(primary_key=True, serialize=False)),
                ('submitted', models.IntegerField()),
                ('modid', models.IntegerField(db_column='ModID')),
                ('steamid', models.CharField(db_column='SteamId', max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('reason', models.TextField()),
                ('ip', models.CharField(max_length=64)),
                ('subname', models.CharField(blank=True, max_length=128, null=True)),
                ('sip', models.CharField(blank=True, max_length=64, null=True)),
                ('archiv', models.IntegerField(blank=True, null=True)),
                ('archivedby', models.IntegerField(blank=True, null=True)),
                ('server', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sb_submissions',
                'managed': False,
            },
        ),
    ]
