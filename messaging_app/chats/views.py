from django.shortcuts import render
from rest_framework import viewsets
from chats.models import Message, Conversation
from chats.serializers import MessageSerializer, ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer