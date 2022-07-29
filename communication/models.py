from re import T
from django.db import models
from users.models import Course, CustomUser
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Reply(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    parent = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='received_messages')

    def __str__(self):
        return self.content

