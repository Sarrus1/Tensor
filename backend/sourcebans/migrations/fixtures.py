# This file adds test data to the migrations
import os
from django.conf import settings
from django.db import migrations
from sourcebans.models import *
import json
from pathlib import Path


def create_groups(apps, schema_editor):
    with open(os.path.join(Path(__file__).parent.parent,  "fixtures", "SbGroupsFixtures.json")) as f:
        dummyGroups = json.load(f)

    for group in dummyGroups:
        newGroup = SbGroups.objects.create(
            **group
        )


def create_admins(apps, schema_editor):
    with open(os.path.join(Path(__file__).parent.parent,  "fixtures", "SbAdminsFixtures.json")) as f:
        dummyAdmins = json.load(f)

    for admin in dummyAdmins:
        group = SbGroups.objects.get(gid=admin["gid"])
        del admin["gid"]
        newAdmin = SbAdmins.objects.create(
            gid=group,
            **admin
        )


if settings.DEBUG:

    class Migration(migrations.Migration):

        dependencies = [
            ('sourcebans', "0002_auto_20210714_1507"),
        ]

        operations = [
            migrations.RunPython(create_groups),
            migrations.RunPython(create_admins)
        ]
else:
    class Migration(migrations.Migration):

        dependencies = [
            ('sourcebans', "0002_auto_20210714_1507"),
        ]

        operations = [
        ]
