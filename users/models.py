from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

class CustomUser(AbstractUser):
    role = models.PositiveIntegerField(choices=ROLE_CHOICES,default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
