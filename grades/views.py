from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from grades.forms import GradeUploadForm

from grades.models import CourseGrade, GradeFile
from users.models import Course, CustomUser
from django.shortcuts import render,redirect
from django.contrib import messages

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
    for beta in thiscoursegrades:
        thiscoursepercents.append(beta.percentage)
        sum += beta.percentage
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

@login_required
def gradeupload(request,courseid):
    course = Course.objects.filter(pk=courseid).first()
    if request.method == 'POST':
        form = GradeUploadForm(request.POST,request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            file_data = csv_file.read().decode("utf-8")	
            # ID, grade
            lines = file_data.split("\r\n")
            print(lines)
            for line in lines:
                if line != '':
                    fields = line.split(",")
                    personid = int(fields[0][2:])
                    grade = int(fields[1])
                    print(personid)
                    print(grade)
                    person = CustomUser.objects.filter(pk=personid).first()
                    try:
                        persongrade = CourseGrade.objects.filter(student=person,course=course).first()
                        persongrade.grade = grade
                        persongrade.save()
                    except:
                        CourseGrade.objects.create(student=person,course=course,percentage=0,grade=grade)
            messages.success(request, f'Bulk Upload Complete')
            return redirect('course-detail',pk=course.pk)
    else:
        form = GradeUploadForm()
        return render(request,'grades/gradeupload.html',{'form': form,})    
                
                





