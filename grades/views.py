from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from grades.models import CourseGrade
from users.models import Course

@login_required
def gradeview(request,courseid):
    student = request.user
    course = Course.objects.filter(pk=courseid).first()
    if not CourseGrade.objects.filter(course=course,student=student):
        CourseGrade.objects.create(course=course,student=student,percentage=0.00)
    grade = CourseGrade.objects.filter(course=course,student=student).first()

    thiscoursegrades = CourseGrade.objects.filter(course=course)
    thiscoursepercents = []
    sum = 0
    number = 0
    for grade in thiscoursegrades:
        thiscoursepercents.append(grade.percentage)
        sum += grade.percentage
        number += 1

    average = sum/number
    maximum = max(thiscoursepercents)
    context = {
        'grade': grade,
        'coursestudents': course.students.all(),
        'average': average,
        'maximum': maximum,
        'course': course
    }

    return render(request,'grades/gradeview.html',context)
