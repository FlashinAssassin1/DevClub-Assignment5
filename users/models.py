from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

class CustomUser(AbstractUser):
    role = models.PositiveIntegerField(choices=ROLE_CHOICES,default=1)
    description = models.TextField(max_length=200,default='Hi!')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=6)
    participants = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.code

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

