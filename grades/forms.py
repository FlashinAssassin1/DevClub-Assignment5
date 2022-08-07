from django import forms

from grades.models import GradeFile

class GradeUploadForm(forms.ModelForm):
    file = forms.FileField(label='Upload CSV File in ID, Grade format')
    
    class Meta():
        model = GradeFile
        fields = ['file']