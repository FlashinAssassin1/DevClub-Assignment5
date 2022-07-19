from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
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

def home(request):
    currentuser = request.user
    courses = currentuser.course_set.all()
    context = {
        'courses': courses,
    }
    return render(request, 'users/home.html',context)

class StudentCourseListView(ListView):
    model = Course
    template_name = 'users/home.html' # app/model_viewtype.html
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        currentuser = self.request.user
        return currentuser.course_set.all()

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

