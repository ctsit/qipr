from __future__ import unicode_literals

from django.apps import AppConfig


class RegistryConfig(AppConfig):
    name = 'registry'

    def ready(self):
        from registry.signals import all_signals
