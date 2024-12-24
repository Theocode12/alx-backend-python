from rest_framework import serializers
from chats import Conversation, Message, User

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    receiver_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    conversation_id = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'receiver_id', 'message_body', 'sent_at', 'conversation_id']

class ConversationSerializer(serializers.ModelSerializer):
    message_set = MessageSerializer(many=True)
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, pk_field=serializers.UUIDField(format='hex'))
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'created_at', 'message_set', 'participants']
