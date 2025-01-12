from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Notification, Message

@receiver(post_save, sender=Message)
def notify(sender, **kwargs):
    Notification.objects.create(receiver=sender.receiver, message=sender)