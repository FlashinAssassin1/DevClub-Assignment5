from django.db import models
from django.urls import reverse
from users.models import Course, CustomUser
from django.utils import timezone

class Quiz(models.Model):
    # title = models.CharField(max_length=50,default="New Quiz")
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    weightage = models.FloatField("Weightage(in %)")
    duration = models.IntegerField("Duration in minutes")
    startafter_time = models.DateTimeField("Start After Time: (format:dd-mm-yyyy HH-MM")
    startbefore_time = models.DateTimeField("Start Before Time: (format:dd-mm-yyyy HH-MM")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz-view', kwargs={'pk': self.pk,'courseid': self.course.pk})

class Question(models.Model):
    question = models.CharField(max_length=300)
    marks = models.IntegerField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questionbank')
    optionA = models.CharField(max_length=300)
    optionB = models.CharField(max_length=300)
    optionC = models.CharField(max_length=300)
    optionD = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    
    def __str__(self):
        return self.question

class QuizAttempt(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    quiz = models.OneToOneField(Quiz,on_delete=models.CASCADE)
    score = models.IntegerField()
    percentage = models.FloatField()
    time_taken = models.IntegerField()
    correct_answers = models.PositiveSmallIntegerField()
    incorrect_answers = models.PositiveSmallIntegerField()
    total_marks = models.PositiveSmallIntegerField()
    end_time = models.DateTimeField(default=timezone.now)
