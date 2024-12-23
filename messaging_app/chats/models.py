from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        GUEST = ('guest', _('Guest'))
        HOST = ('host', _('Host'))
        ADMIN = ('admin', _('Admin'))

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(choices=Role, max_length=7)

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants = models.ManyToManyField('User', db_column='participants_id')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey('User', models.CASCADE, related_name='sender', db_column='sender_id')
    receiver = models.ForeignKey('User', models.CASCADE, related_name='receiver', db_column='reciever_id')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey('Conversation', models.CASCADE, db_column='conversation_id')
