from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Course, CustomUser,Profile

GEEKS_CHOICES =(
    ("1", "Student"),
    ("2", "Teacher"),
)

class UserRegisterForm(UserCreationForm):
    type = forms.ChoiceField(choices=GEEKS_CHOICES)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    

    class Meta():
        model = CustomUser
        fields = ['username','type','first_name','last_name','description','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = CustomUser
        fields = ['username','email','description']    

class ProfileUpdateForm(forms.ModelForm):
     class Meta():
        model = Profile
        fields = ['image']

class CourseForm(forms.ModelForm):

    teachers = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(type=2),
        widget=forms.CheckboxSelectMultiple
    )
    students = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(type=1),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta():
        model = Course
        fields = ['code','title','desc','teachers','students']

class CourseTeacherForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ['code','title','desc']