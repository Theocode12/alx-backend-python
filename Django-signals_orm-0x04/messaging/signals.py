from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Notification, Message, MessageHistory

@receiver(post_save, sender=Message)
def notify(sender: Message, **kwargs):
    Notification.objects.create(receiver=sender.receiver, message=sender)


@receiver(pre_save, sender=Message)
def loggingMessageHistory(sender: Message, **kwargs):
    MessageHistory.objects.create(sender=sender.sender, receiver=sender.receiver, content=sender.content, edited=sender.edited, timestamp=sender.timestamp)