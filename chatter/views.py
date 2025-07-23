from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .models import MessageModel,MessageStatus,ChatroomModel
from .serializers import MessageSerializer,MessageStatusSerializer,ChatRoomSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset=ChatroomModel.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
class MessageStatusViewSet(viewsets.ModelViewSet):
    queryset=MessageStatus.objects.all()
    serializer_class=MessageStatusSerializer
    permission_classes=[permissions.IsAuthenticated]
        
        