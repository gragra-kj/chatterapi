from django.contrib import admin

# Register your models here.
from .models import ChatroomModel,MessageModel,MessageStatus

admin.site.register(ChatroomModel)
admin.site.register(MessageModel)
admin.site.register(MessageStatus)