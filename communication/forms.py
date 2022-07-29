from django import forms
from .models import Message, Reply

class CreateReplyForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = ['title','content']

class CreateMessageForm(forms.ModelForm):
    class Meta():
        model = Message
        fields = ['content']