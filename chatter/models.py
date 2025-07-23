from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ChatroomModel(models.Model):
    name=models.CharField(max_length=100)
    participant=models.ManyToManyField(User,related_name='chatroom')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class MessageModel(models.Model):
    chat_room=models.ForeignKey(ChatroomModel,on_delete=models.CASCADE)
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    time_stamp=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat_room.name}"

    
class MessageStatus(models.Model):
    message=models.ForeignKey(MessageModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_read=models.BooleanField(default=False)
    read_at=models.DateTimeField(null=True,blank=True)   
    
    def __str__(self):
        return f"{self.user.username} read status for message {self.message.id}"     
    
