from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from .models import Notification, Message, MessageHistory, User

@receiver(post_save, sender=Message)
def notify(sender: Message, **kwargs):
    Notification.objects.create(receiver=sender.receiver, message=sender)


@receiver(pre_save, sender=Message)
def loggingMessageHistory(sender: Message, **kwargs):
    MessageHistory.objects.create(
        edited_by=sender.sender, 
        receiver=sender.receiver, 
        content=sender.content, 
        )
    
@receiver(post_delete, sender=User)
def clean_up_user_related_data(sender: User, **kwargs):
    Message.objects.filter(sender=sender).delete()
    Message.objects.filter(receiver=sender).delete()