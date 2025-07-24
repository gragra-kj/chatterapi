from rest_framework import serializers
from .models import ChatroomModel,MessageModel,MessageStatus
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatRoomSerializer(serializers.ModelSerializer):
    participant = UserSerializer(many=True, read_only=True)
    class Meta:
        model=ChatroomModel
        fields=['id','name','participant','created_at','updated_at']
        
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')  
    chat_room = serializers.PrimaryKeyRelatedField(queryset=ChatroomModel.objects.all())
    class Meta:
        model = MessageModel
        fields = ['id', 'chat_room', 'sender', 'content', 'time_stamp', 'read']

    def create(self, validated_data):
        user = self.context['request'].user  
        validated_data['sender'] = user
        return super().create(validated_data)
        
# class MessageStatusSerializer(serializers.ModelSerializer):
#     message = MessageSerializer(read_only=True)
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model=MessageStatus
#         fields=['id','message','user','is_read','read_at']        
class MessageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageStatus
        fields = ['id', 'message', 'user', 'is_read', 'read_at']
