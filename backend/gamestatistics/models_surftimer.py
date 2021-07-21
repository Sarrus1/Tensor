from django.db import models


class CkAnnouncements(models.Model):
    server = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    mapname = models.CharField(max_length=128)
    mode = models.IntegerField()
    time = models.CharField(max_length=32)
    group = models.IntegerField()
    style = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_announcements'


class CkBonus(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    mapname = models.CharField(max_length=32)
    runtime = models.FloatField()
    zonegroup = models.IntegerField()
    style = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_bonus'
        unique_together = (('steamid', 'mapname', 'zonegroup', 'style'),)


class CkCheckpoints(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    mapname = models.CharField(max_length=32)
    cp1 = models.FloatField(blank=True, null=True)
    cp2 = models.FloatField(blank=True, null=True)
    cp3 = models.FloatField(blank=True, null=True)
    cp4 = models.FloatField(blank=True, null=True)
    cp5 = models.FloatField(blank=True, null=True)
    cp6 = models.FloatField(blank=True, null=True)
    cp7 = models.FloatField(blank=True, null=True)
    cp8 = models.FloatField(blank=True, null=True)
    cp9 = models.FloatField(blank=True, null=True)
    cp10 = models.FloatField(blank=True, null=True)
    cp11 = models.FloatField(blank=True, null=True)
    cp12 = models.FloatField(blank=True, null=True)
    cp13 = models.FloatField(blank=True, null=True)
    cp14 = models.FloatField(blank=True, null=True)
    cp15 = models.FloatField(blank=True, null=True)
    cp16 = models.FloatField(blank=True, null=True)
    cp17 = models.FloatField(blank=True, null=True)
    cp18 = models.FloatField(blank=True, null=True)
    cp19 = models.FloatField(blank=True, null=True)
    cp20 = models.FloatField(blank=True, null=True)
    cp21 = models.FloatField(blank=True, null=True)
    cp22 = models.FloatField(blank=True, null=True)
    cp23 = models.FloatField(blank=True, null=True)
    cp24 = models.FloatField(blank=True, null=True)
    cp25 = models.FloatField(blank=True, null=True)
    cp26 = models.FloatField(blank=True, null=True)
    cp27 = models.FloatField(blank=True, null=True)
    cp28 = models.FloatField(blank=True, null=True)
    cp29 = models.FloatField(blank=True, null=True)
    cp30 = models.FloatField(blank=True, null=True)
    cp31 = models.FloatField(blank=True, null=True)
    cp32 = models.FloatField(blank=True, null=True)
    cp33 = models.FloatField(blank=True, null=True)
    cp34 = models.FloatField(blank=True, null=True)
    cp35 = models.FloatField(blank=True, null=True)
    zonegroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_checkpoints'
        unique_together = (('steamid', 'mapname', 'zonegroup'),)


class CkLatestrecords(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    runtime = models.FloatField()
    map = models.CharField(max_length=32)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ck_latestrecords'
        unique_together = (('steamid', 'map', 'date'),)


class CkMaptier(models.Model):
    mapname = models.CharField(primary_key=True, max_length=54)
    tier = models.IntegerField()
    maxvelocity = models.FloatField()
    announcerecord = models.IntegerField()
    gravityfix = models.IntegerField()
    ranked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_maptier'


class CkNewmaps(models.Model):
    mapname = models.CharField(primary_key=True, max_length=32)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ck_newmaps'


class CkPlayeroptions2(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    timer = models.IntegerField()
    hide = models.IntegerField()
    sounds = models.IntegerField()
    chat = models.IntegerField()
    viewmodel = models.IntegerField()
    autobhop = models.IntegerField()
    checkpoints = models.IntegerField()
    gradient = models.IntegerField()
    speedmode = models.IntegerField()
    centrespeed = models.IntegerField()
    centrehud = models.IntegerField()
    teleside = models.IntegerField()
    module1c = models.IntegerField()
    module2c = models.IntegerField()
    module3c = models.IntegerField()
    module4c = models.IntegerField()
    module5c = models.IntegerField()
    module6c = models.IntegerField()
    sidehud = models.IntegerField()
    module1s = models.IntegerField()
    module2s = models.IntegerField()
    module3s = models.IntegerField()
    module4s = models.IntegerField()
    module5s = models.IntegerField()
    prestrafe = models.IntegerField()
    cpmessages = models.IntegerField()
    wrcpmessages = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_playeroptions2'


class CkPlayerrank(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    steamid64 = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    wrpoints = models.IntegerField()
    wrbpoints = models.IntegerField()
    wrcppoints = models.IntegerField()
    top10points = models.IntegerField()
    groupspoints = models.IntegerField()
    mappoints = models.IntegerField()
    bonuspoints = models.IntegerField()
    finishedmaps = models.IntegerField(blank=True, null=True)
    finishedmapspro = models.IntegerField(blank=True, null=True)
    finishedbonuses = models.IntegerField()
    finishedstages = models.IntegerField()
    wrs = models.IntegerField()
    wrbs = models.IntegerField()
    wrcps = models.IntegerField()
    top10s = models.IntegerField()
    groups = models.IntegerField()
    lastseen = models.IntegerField(blank=True, null=True)
    joined = models.IntegerField()
    timealive = models.IntegerField()
    timespec = models.IntegerField()
    connections = models.IntegerField()
    readchangelog = models.IntegerField()
    style = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_playerrank'
        unique_together = (('steamid', 'style'),)


class CkPlayertemp(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    mapname = models.CharField(max_length=32)
    cords1 = models.FloatField()
    cords2 = models.FloatField()
    cords3 = models.FloatField()
    angle1 = models.FloatField()
    angle2 = models.FloatField()
    angle3 = models.FloatField()
    enctickrate = models.IntegerField(db_column='EncTickrate', blank=True, null=True)  # Field name made lowercase.
    runtimetmp = models.FloatField(db_column='runtimeTmp')  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.
    zonegroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_playertemp'
        unique_together = (('steamid', 'mapname'),)


class CkPlayertimes(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    mapname = models.CharField(max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    runtimepro = models.FloatField()
    style = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_playertimes'
        unique_together = (('steamid', 'mapname', 'style'),)


class CkSpawnlocations(models.Model):
    mapname = models.CharField(primary_key=True, max_length=54)
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    pos_z = models.FloatField()
    ang_x = models.FloatField()
    ang_y = models.FloatField()
    ang_z = models.FloatField()
    vel_x = models.FloatField()
    vel_y = models.FloatField()
    vel_z = models.FloatField()
    zonegroup = models.IntegerField()
    stage = models.IntegerField()
    teleside = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_spawnlocations'
        unique_together = (('mapname', 'zonegroup', 'stage', 'teleside'),)


class CkVipadmins(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=128, blank=True, null=True)
    namecolour = models.IntegerField(blank=True, null=True)
    textcolour = models.IntegerField()
    joinmsg = models.CharField(max_length=255, blank=True, null=True)
    pbsound = models.CharField(max_length=256)
    topsound = models.CharField(max_length=256)
    wrsound = models.CharField(max_length=256)
    inuse = models.IntegerField(blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    admin = models.IntegerField()
    zoner = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_vipadmins'


class CkWrcps(models.Model):
    steamid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, blank=True, null=True)
    mapname = models.CharField(max_length=32)
    runtimepro = models.FloatField()
    stage = models.IntegerField()
    style = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_wrcps'
        unique_together = (('steamid', 'mapname', 'stage', 'style'),)


class CkZones(models.Model):
    mapname = models.CharField(primary_key=True, max_length=54)
    zoneid = models.IntegerField()
    zonetype = models.IntegerField(blank=True, null=True)
    zonetypeid = models.IntegerField(blank=True, null=True)
    pointa_x = models.FloatField(blank=True, null=True)
    pointa_y = models.FloatField(blank=True, null=True)
    pointa_z = models.FloatField(blank=True, null=True)
    pointb_x = models.FloatField(blank=True, null=True)
    pointb_y = models.FloatField(blank=True, null=True)
    pointb_z = models.FloatField(blank=True, null=True)
    vis = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    zonegroup = models.IntegerField()
    zonename = models.CharField(max_length=128, blank=True, null=True)
    hookname = models.CharField(max_length=128, blank=True, null=True)
    targetname = models.CharField(max_length=128, blank=True, null=True)
    onejumplimit = models.IntegerField()
    prespeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ck_zones'
        unique_together = (('mapname', 'zoneid'),)
