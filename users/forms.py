from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser,Profile

GEEKS_CHOICES =(
    ("1", "Student"),
    ("2", "Teacher"),
)

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=GEEKS_CHOICES)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    

    class Meta():
        model = CustomUser
        fields = ['username','role','first_name','last_name','description','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = CustomUser
        fields = ['username','email','description']    

class ProfileUpdateForm(forms.ModelForm):
     class Meta():
        model = Profile
        fields = ['image']