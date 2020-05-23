from django.apps import AppConfig


class HosmngConfig(AppConfig):
    name = 'hosmng'

    def ready(self):
     	import hosmng.signals