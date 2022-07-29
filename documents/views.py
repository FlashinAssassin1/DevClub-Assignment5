from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from documents.forms import DocumentForm
from documents.models import Document
from users.models import Course
import os
from django.contrib.auth.decorators import login_required

class DocumentCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Document
    form_class = DocumentForm

    def test_func(self):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        if self.request.user in course.teachers.all():
            return True
        return False

    def form_valid(self, form):
        courseid = self.kwargs['courseid']
        currentuser = self.request.user
        form.instance.author = currentuser
        form.instance.course = Course.objects.filter(pk=courseid).first()
        filename = os.path.basename(form.instance.file.name)
        filedict = {
            'pdf': 'filetype_pics/pdf.jpg',
            'docx': 'filetype_pics/document.jpg',
            'txt': 'filetype_pics/text.jpg',
            'pptx': 'filetype_pics/powerpoint.jpg',
            'zip': 'filetype_pics/archive.jpg',
            'xlsx': 'filetype_pics/spreadsheet.jpg',
        }
        filetype = filename.split('.')[1]
        if filetype in filedict:
            form.instance.filetype = filedict[filetype]
        return super().form_valid(form)

class DocumentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Document
    form_class = DocumentForm
    
    def test_func(self):
        doc = self.get_object()
        if self.request.user == doc.author:
            return True
        return False

class DocumentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Document
    success_url = '/'

    def test_func(self):
        doc = self.get_object()
        if self.request.user == doc.author:
            return True
        return False

class DocumentDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Document

    def test_func(self):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        if self.request.user in course.teachers.all() | course.students.all():
            return True
        return False

class DocumentListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Document
    context_object_name = 'documents'
    ordering = ['-date_modified']

    def test_func(self):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        if self.request.user in course.teachers.all() | course.students.all():
            return True
        return False

@login_required
def documentlist(request,courseid):
    course = Course.objects.filter(pk=courseid).first()
    documents = Document.objects.filter(course=course).order_by('-date_modified')

    context = {
        'course': course,
        'coursepeople': course.teachers.all() | course.students.all(),
        'documents': documents,
    }
    return render(request,'documents/document_list.html',context)


