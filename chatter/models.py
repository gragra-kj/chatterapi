from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ChatroomModel(models.Model):
    name=models.CharField(max_length=100)
    participant=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
class MessageModel(models.Model):
    chat_room=models.ForeignKey(ChatroomModel,on_delete=models.CASCADE)
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    time_stamp=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)
    
class MessageStatus(models.Model):
    message=models.ForeignKey(MessageModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_read=models.BooleanField(default=False)
    read_at=models.DateTimeField(auto_now_add=True)        
