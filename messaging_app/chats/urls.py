from django.urls import path, include
from chats.views import MessageViewSet, ConversationViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('messages', MessageViewSet)
routers.register('conversations', ConversationViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)