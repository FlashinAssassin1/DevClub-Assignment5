from email.policy import default
from django.db import models
from users.models import Course, CustomUser
from django.utils import timezone
import os
from django.urls import reverse

class Document(models.Model):
    file = models.FileField(upload_to='lecture_notes')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    visible_name = models.CharField(max_length=50)
    filetype = models.ImageField(default='filetype_pics/unknown.jpg')

    def __str__(self):
        return self.visible_name
    
    def get_absolute_url(self):
        return reverse('document-detail', kwargs={'pk': self.pk,'courseid': self.course.pk})

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' KB'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' MB'
        else:
            value = round(x/1000000000, 2)
            ext = ' GB'
        return str(value)+ext
    
    @property
    def actualfilename(self):
        return os.path.basename(self.file.name)
