from django import forms
from .models import Room, Message

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = {'user', 'user_read', 'admin_read', }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = {'body',}