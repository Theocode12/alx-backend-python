from django.apps import AppConfig
from django.db.models.signals import post_save
from .models import Message

class MessagingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "messaging"

    def ready(self):
        from . import signals

        post_save.connect(signals.notify, Message)
