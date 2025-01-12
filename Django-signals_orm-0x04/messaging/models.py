from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE, db_column='sender_id')
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, db_column='reciever_id')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    edited = models.BooleanField()
    unread = models.BooleanField()
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE)

class Notification(models.Model):
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, db_column='reciever_id')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, db_column='message_id')

class MessageHistory(models.Model):
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='sender_id')
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, db_column='reciever_id')
    content = models.TextField()
    edited_at = models.DateTimeField(auto_now=True)
