from django.apps import AppConfig


class DonationsConfig(AppConfig):
    name = 'donations'

    def ready(self):
        import donations.signals