# Tout ce code est un snippet volé sur plusieurs threads Stackoverflow
# Il permet de créer un décorateur qui vérifie si un utilisateur est bien identifié,
# et le redirige vers la page de login sinon. Django ne fait pas cette dernière partie seul...

try:
		from functools import wraps
except ImportError:
		from django.utils.functional import wraps  # Python 2.4 fallback.
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from steam.steamid import SteamID
from sourcebans.models import SbAdmins

default_message = "You must login first"


def user_passes_test(test_func, message=default_message):
		"""
		Decorator for views that checks that the user passes the given test,
		setting a message in case of no success. The test should be a callable
		that takes the user object and returns True if the user passes.
		"""
		def decorator(view_func):
				def _wrapped_view(request, *args, **kwargs):
						if not test_func(request.user):
								messages.error(request, message)
						return view_func(request, *args, **kwargs)
				return _wrapped_view
		return decorator


def login_required_message(function=None, message=default_message):
		"""
		Decorator for views that checks that the user is logged in, redirecting
		to the log-in page if necessary.
		"""
		actual_decorator = user_passes_test(
				lambda u: u.is_authenticated,
				message=message,
		)
		if function:
				return actual_decorator(function)
		return actual_decorator


def login_required_messsage_and_redirect(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None, message=default_message):

		if function:
				return login_required_message(
						login_required(function, redirect_field_name, login_url),
						message
				)

		return lambda deferred_function: login_required_message_and_redirect(deferred_function, redirect_field_name, login_url, message)



def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
		"""
		Decorator for views that checks that the user is logged in, redirecting
		to the log-in page if necessary.
		"""
		def is_admin(u):
				if u.is_authenticated:
						steamid = SteamID(u.steamid).as_steam2
						Results = SbAdmins.objects.get(authid=steamid)
						if Results or u.is_superuser:
								return True
				return False

		actual_decorator = user_passes_test(
				lambda u: is_admin(u)
		)
		if function:
				return actual_decorator(function)
		return actual_decorator