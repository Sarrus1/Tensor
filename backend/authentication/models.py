from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from steam.steamid import SteamID
from sourcebans.models import SbAdmins


class SteamUserManager(BaseUserManager):
		def _create_user(self, steamid, password, **extra_fields):
				"""
				Creates and saves a User with the given steamid and password.
				"""
				try:
						# python social auth provides an empty email param, which cannot be used here
						del extra_fields['email']
				except KeyError:
						pass
				if not steamid:
						raise ValueError('The given steamid must be set')
				user = self.model(steamid=steamid, **extra_fields)
				user.set_password(password)
				user.save(using=self._db)
				return user

		def create_user(self, steamid, password=None, **extra_fields):
				extra_fields.setdefault('is_staff', False)
				extra_fields.setdefault('is_superuser', False)
				return self._create_user(steamid, password, **extra_fields)

		def create_superuser(self, steamid, password, **extra_fields):
				extra_fields.setdefault('is_staff', True)
				extra_fields.setdefault('is_superuser', True)

				if extra_fields.get('is_staff') is not True:
						raise ValueError('Superuser must have is_staff=True.')
				if extra_fields.get('is_superuser') is not True:
						raise ValueError('Superuser must have is_superuser=True.')

				return self._create_user(steamid, password, **extra_fields)


class SteamUser(AbstractBaseUser, PermissionsMixin):
		USERNAME_FIELD = 'steamid'

		steamid = models.CharField(max_length=30, unique=True)
		personaname = models.CharField(max_length=255)
		profileurl = models.CharField(max_length=300)
		avatar = models.CharField(max_length=255)
		avatarmedium = models.CharField(max_length=255)
		avatarfull = models.CharField(max_length=255)
		can_control = models.BooleanField("Can control the servers", default = False)
		can_accept_awp = models.BooleanField("Can accept awp applications", default = False)
		can_accept_retake = models.BooleanField("Can accept retake applications", default = False)
		loccountrycode = models.CharField(max_length=20, default="N/A")
		# Add the other fields that can be retrieved from the Web-API if required

		date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
		is_active = models.BooleanField(default=True)
		is_staff = models.BooleanField(default=False)

		objects = SteamUserManager()

		@property
		def get_short_name(self):
				return self.personaname

		@property
		def get_full_name(self):
				return self.personaname

		@property
		def steamid2(self):
				return SteamID(self.steamid).as_steam2

		@property
		def is_admin(self):
				q = SbAdmins.objects.filter(authid__icontains=self.steamid2)
				return bool(q)
		
		@property
		def sb_admin_id(self):
				q = SbAdmins.objects.filter(authid__icontains=self.steamid2)
				return q[0].aid