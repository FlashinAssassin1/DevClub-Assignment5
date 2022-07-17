from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import CustomUser

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
        fields = ['username','role','first_name','last_name','email','password1','password2']