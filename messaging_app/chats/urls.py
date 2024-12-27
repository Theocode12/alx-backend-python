from django.urls import path, include
from chats.views import MessageViewSet, ConversationViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter

conv_router = routers.DefaultRouter()
conv_router.register(r'conversations', ConversationViewSet)

message_router = NestedDefaultRouter(conv_router, r'conversations', lookup='conversations')
message_router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(conv_router.urls)),
    path('', include(message_router.urls)),
]

# this line was commented out as it was causing some errors
# urlpatterns = format_suffix_patterns(urlpatterns)
