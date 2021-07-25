from gamestatistics.models import *
from donations.models import *

# Ce fichier permet de router les différents modèles stockés dans des BDD externes.


class router(object):

		def db_for_read(self, model, **hints):
				# Ici on associe chaque modèle à sa bdd pour la lecture.
				if model in [Rank_awp, RankAwpSeason, RankAwpSeasonId]:
						return 'rank_awp'
				if model == Rank_retake:
						return 'rank_retake'
				if model in [CkPlayertimes, CkWrcps, CkPlayertemp, CkPlayerrank, CkPlayeroptions2, CkNewmaps, CkMaptier, CkLatestrecords, CkBonus, CkAnnouncements]:
						return 'surftimer'
				if model._meta.app_label == 'sourcebans':
						return 'sourcebans'
				if model == Tvip:
						return 'tvip'
				return 'default'

		def db_for_write(self, model, **hints):
				# Ici on associe chaque modèle à sa bdd pour l'écriture.
				if model == Rank_awp:
						return 'rank_awp'
				if model == Rank_retake:
						return 'rank_retake'
				if model == CkPlayertimes:
						return 'surftimer'
				if model._meta.app_label == 'sourcebans':
						return 'sourcebans'
				if model == Tvip:
						return 'tvip'
				return 'default'

		def allow_migrate(self, db, app_label, model_name=None, **hints):
				# Ici on associe chaque modèle à sa bdd pour les migrations.
				return db == 'default'
