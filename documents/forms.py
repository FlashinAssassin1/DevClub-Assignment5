from django import forms

from documents.models import Document

class DocumentForm(forms.ModelForm):

    visible_name = forms.CharField(max_length=50,label='FileName')

    class Meta():
        model = Document
        fields = ['file','visible_name']