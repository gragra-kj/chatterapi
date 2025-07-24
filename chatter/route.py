from rest_framework.routers import DefaultRouter
from .views import ChatRoomViewSet,MessageStatusViewSet,MessageViewSet
from django.urls import path,include

router=DefaultRouter()
router.register('chatroom',ChatRoomViewSet)
router.register('messagestatus',MessageStatusViewSet)
router.register('messages',MessageViewSet)

urlpatterns=[
    path('',include(router.urls))
]