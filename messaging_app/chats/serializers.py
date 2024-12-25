from rest_framework import serializers
from .models import Conversation, Message, User

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    receiver_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    conversation_id = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    message_body = serializers.CharField(style={'base_template': 'textarea.html'})
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'receiver_id', 'message_body', 'sent_at', 'conversation_id']

class ConversationSerializer(serializers.ModelSerializer):
    message_set = serializers.SerializerMethodField()
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, pk_field=serializers.UUIDField(format='hex'))
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'created_at', 'message_set', 'participants']
   
    def get_message_set(self, obj):
        messages = Message.objects.all()
        filtered_messages = messages.filter(conversation_id=obj.id)
        serialized_messages = MessageSerializer(filtered_messages, many=True)
        return serialized_messages.data

    def validate_participants(self, value):
        if len(participants) != 2:
            raise serializers.ValidationError("participants must be 2 or more")
        return value
