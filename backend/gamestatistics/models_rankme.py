from django.db import models
from django.utils.safestring import mark_safe

class RankMeModel(models.Model):
		steam = models.CharField(unique=True, max_length=40, blank=True, primary_key=True)
		name = models.TextField(blank=True, null=True)
		lastip = models.TextField(blank=True, null=True)
		score = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		kills = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		deaths = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		assists = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		suicides = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		tk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		shots = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		hits = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		headshots = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		connected = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		rounds_tr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		rounds_ct = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		lastconnect = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		knife = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		glock = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		hkp2000 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		usp_silencer = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		p250 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		deagle = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		elite = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		fiveseven = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		tec9 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		cz75a = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		revolver = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		nova = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		xm1014 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mag7 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		sawedoff = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		bizon = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mac10 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mp9 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mp7 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		ump45 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		p90 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		galilar = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		ak47 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		scar20 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		famas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		m4a1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		m4a1_silencer = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		aug = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		ssg08 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		sg556 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		awp = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		g3sg1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		m249 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		negev = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		hegrenade = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		flashbang = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		smokegrenade = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		inferno = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		decoy = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		taser = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mp5sd = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		breachcharge = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		head = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		chest = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		stomach = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		left_arm = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		right_arm = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		left_leg = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		right_leg = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		c4_planted = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		c4_exploded = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		c4_defused = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		ct_win = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		tr_win = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		hostages_rescued = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		vip_killed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		vip_escaped = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		vip_played = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		mvp = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		damage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		match_win = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		match_draw = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		match_lose = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		first_blood = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		no_scope = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
		no_scope_dis = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

		class Meta:
				abstract=True
				managed = False
				app_label = 'gamestatistics'
				db_table = 'rankme'
		
		def __str__(self):
				return str(self.steam) if self.steam else ''

		def KDcalculator(self):
				if self.deaths == 0:
					KD = self.kills
				else:
					KD = round(self.kills/self.deaths, 3)
				return KD

		def ADRcalculator(self):
				if self.rounds_ct+self.rounds_tr == 0:
					ADR = self.damage
				else:
					ADR = round(self.damage/(self.rounds_ct+self.rounds_tr), 3)
				return(ADR)

		def steamid_to_profile(self):
				url = str(self.steam)
				url = "<a type='button' href='/stats/awp/" + url
				button = url + "' class='btn btn-block btn-info'>Profile</a>"
				return mark_safe(button)

		def time(self):
				time = self.connected
				hour = time//3600
				minute = str((time - hour*3600)//60)+"m"
				return str(hour)+'h'+minute

		def total(self):
				return self.connected


class RankMeSeasonIdModel(models.Model):
		season_id = models.AutoField(primary_key=True)
		start_date = models.DateTimeField(blank=True, null=True)
		end_date = models.DateTimeField(blank=True, null=True)

		class Meta:
				managed = False
				db_table = 'rankme_season_id'
				abstract = True


class Rank_awp(RankMeModel):
		pass


class RankAwpSeasonId(RankMeSeasonIdModel):
		pass


class RankAwpSeason(RankMeModel):
		season_id = models.ForeignKey(RankAwpSeasonId, on_delete=models.DO_NOTHING, db_column='season_id')

		
		class Meta(RankMeModel.Meta):
				db_table = 'rankme_season'


class Rank_retake(RankMeModel):
		pass
