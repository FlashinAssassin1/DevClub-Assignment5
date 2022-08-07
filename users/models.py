from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Admin'),
    )

class CustomUser(AbstractUser):
    type = models.PositiveIntegerField(choices=TYPE_CHOICES,default=1)
    description = models.TextField(max_length=200,default='Hi!')

    def __str__(self):
         
        return f'{self.first_name} {self.last_name}'
    
class Course(models.Model):
    code = models.CharField(max_length=6,unique=True)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000,default='Base Text')
    coursepic = models.ImageField(default='coursedefault.jpg',upload_to='course_pics')
    creator = models.ForeignKey(CustomUser,limit_choices_to={'type': 3},on_delete=models.PROTECT,related_name='created_courses')
    teachers = models.ManyToManyField(CustomUser,limit_choices_to={'type': 2},related_name='teachcourses')
    students = models.ManyToManyField(CustomUser,limit_choices_to={'type': 1},related_name='studycourses')

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

