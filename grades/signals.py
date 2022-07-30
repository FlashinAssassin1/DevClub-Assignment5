from django.db.models.signals import post_save
from django.dispatch import receiver

from quizzes.models import QuizAttempt
from .models import CourseGrade
from users.models import Course

@receiver(post_save, sender=QuizAttempt)
def change_grade(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        quiz = instance.quiz
        course = quiz.course
        if not CourseGrade.objects.filter(course=course,student=student):
            CourseGrade.objects.create(course=course,student=student,percentage=0.00)
        grade = CourseGrade.objects.filter(course=course,student=student).first()
        grade.percentage += (quiz.weightage) * instance.percentage/100
        grade.save()