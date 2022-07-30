from quizzes.models import Question, Quiz
from django import forms

class CreateQuizForm(forms.ModelForm):
    startafter_time = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M'],label="Start After Time: (format:dd-mm-yyyy HH-MM")
    startbefore_time = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M'],label="Start Before Time: (format:dd-mm-yyyy HH-MM")
    class Meta():
        model = Quiz
        fields = ['weightage','startafter_time','startbefore_time']

GEEKS_CHOICES =(
    ("A", "Option A"),
    ("B", "Option B"),
    ("C", "Option C"),
    ("D", "Option D"),
)

class AddQuestionForm(forms.ModelForm):
    answer = forms.ChoiceField(choices=GEEKS_CHOICES)

    class Meta():
        model = Question
        fields = ['question','marks','optionA','optionB','optionC','optionD','answer'] 

        