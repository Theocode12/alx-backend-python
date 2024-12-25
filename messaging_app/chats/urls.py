from django.urls import path, include
from chats.views import MessageViewSet, ConversationViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

conv_router = DefaultRouter()
conv_router.register(r'conversations', ConversationViewSet)

message_router = NestedDefaultRouter(conv_router, r'conversations', 'conversations')
message_router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(conv_router.urls)),
    path('', include(message_router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)