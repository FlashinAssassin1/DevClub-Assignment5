from django.db import models
from users.models import CustomUser,Course

class CourseGrade(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    percentage = models.FloatField()
    grade = models.PositiveSmallIntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.student}-{self.course}-{self.grade}'

class GradeFile(models.Model):
    file = models.FileField(upload_to='csvfiles')
