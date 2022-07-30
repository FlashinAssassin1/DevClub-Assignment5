from django.db import models
from users.models import CustomUser,Course

class CourseGrade(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    percentage = models.FloatField()
    grade = models.PositiveSmallIntegerField(null=True,blank=True)
