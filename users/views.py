from urllib import request
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import CourseForm, CourseTeacherForm, UserRegisterForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import Http404, HttpResponse
from .models import Course,CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

# def home(request):
#     currentuser = request.user
#     if currentuser.is_authenticated:
#         try:
#             if currentuser.type == 1:
#                 courses = currentuser.studycourses.all()
#             elif currentuser.type == 2:
#                 courses = currentuser.teachcourses.all()
#             else:

#         except:
#             courses = []
#     else:
#         courses = []
#     context = {
#         'courses': courses,
#     }
#     return render(request, 'users/home.html',context)

class CourseListView(ListView):
    model = Course
    template_name = 'users/home.html' # app/model_viewtype.html
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        currentuser = self.request.user
        
        if currentuser.is_authenticated:
            try:
                if currentuser.type == 1:
                    return currentuser.studycourses.all().order_by('id')
                elif currentuser.type == 2:
                    return currentuser.teachcourses.all().order_by('id')
                else:
                    return currentuser.created_courses.all().order_by('id')
            except:
                return []
        else:
            return []

@login_required
def profile(request,pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',pk=request.user.pk)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'askeduser': CustomUser.objects.filter(pk=pk).first(),
    }
    return render(request, 'users/profile.html', context)

def coursedetail(request, pk):
    course = Course.objects.filter(pk=pk).first()
    courseteachers = course.teachers.all()
    coursestudents = course.students.all()

    context = {
        'course': course,
        'courseteachers': courseteachers,
        'coursestudents': coursestudents,
    }
    return render(request, 'users/course_detail.html',context)
    
class CourseCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Course
    form_class = CourseForm

    def test_func(self):
        if self.request.user.type == 3:
            return True
        return False

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class AdminCourseUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Course
    form_class = CourseForm
    
    def test_func(self):
        course = self.get_object()
        if self.request.user.type == 3:
            return True
        return False

class CourseUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Course
    form_class = CourseTeacherForm
    
    def test_func(self):
        course = self.get_object()
        if self.request.user in course.teachers.all():
            return True
        return False

class CourseDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Course
    success_url = '/'

    def test_func(self):
        course = self.get_object()
        if self.request.user.type == 3:
            return True
        return False

def coursestudents(request,pk):
    course = Course.objects.filter(pk=pk).first()
    students = course.students.all()
    return render(request,'users/coursestudents.html',{'students': students,'course':course})
