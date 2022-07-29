from multiprocessing import context
from django.dispatch import receiver
from django.shortcuts import render,redirect
from django.db.models.functions import Concat
from django.db.models import Q, Value

from communication.forms import CreateMessageForm, CreateReplyForm
from .models import Message, Post, Reply
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from users.models import Course, CustomUser

class PostDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Post

    def test_func(self):
        post = self.get_object()
        course = post.course
        if self.request.user in (course.teachers.all() | course.students.all()):
            return True
        else:
            return False

@login_required
def postdetail(request,pk):
    post = Post.objects.filter(pk=pk).first()
    course = post.course
        
    
    if request.method == 'POST':
        form = CreateReplyForm(request.POST)
        form.instance.author = request.user
        form.instance.parent = post
        if form.is_valid():
            form.save()
            return redirect('post-detail',pk)
    elif course == None:
        form =CreateReplyForm(initial={'title': f'Re: {post.title}'})
        context = {
        'object': post,
        'replies':post.reply_set.all().order_by('date_posted'),
        'coursepeople': CustomUser.objects.all(),
        'form': form,
        }
    else:
        form =CreateReplyForm(initial={'title': f'Re: {post.title}'})
        try:
            courseteachers = course.teachers.all()
        except:
            courseteachers = set()

        try:
            coursestudents = course.students.all()
        except:
            coursestudents = set()

        context = {
        'object': post,
        'replies':post.reply_set.all().order_by('date_posted'),
        'coursepeople': courseteachers | coursestudents,
        'form': form,
        }

    return render(request,'communication/post_detail.html',context)

class PostCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        courseid = self.kwargs['courseid']
        if (courseid) != 0:
            course = Course.objects.filter(pk=courseid).first()
            form.instance.course = course 
        return super().form_valid(form)
    
    def test_func(self):
        courseid = self.kwargs['courseid']
        if courseid != 0:
            course = Course.objects.filter(pk=courseid).first()
            if self.request.user in (course.teachers.all() | course.students.all()):
                return True
            return False
        else:
            return True


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def postlist(request,courseid):
    if courseid == 0:
        context = {
            'posts': Post.objects.filter(course=None).order_by('-date_posted'),
            'coursepeople': CustomUser.objects.all(),
            'courseid': courseid
        }
    else:
        course = Course.objects.filter(pk=courseid).first()
        context = {
            'posts': Post.objects.filter(course=course).order_by('-date_posted'),
            'coursepeople': course.teachers.all() | course.students.all(),
            'courseid': courseid,
            'coursecode': course.code
        }

    return render(request,'communication/post_list.html',context)

@login_required
def messageslist(request,personid):
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        form.instance.sender = request.user
        form.instance.receiver = CustomUser.objects.filter(pk=personid).first()
        if form.is_valid():
            form.save()
            return redirect('chatlist',personid)
    else:
        currentuser = request.user
        otherperson = CustomUser.objects.filter(pk=personid).first()
        chatlist = (Message.objects.filter(sender=currentuser,receiver=otherperson) | Message.objects.filter(receiver=currentuser,sender=otherperson)).order_by('-date_sent')
        form = CreateMessageForm()
    return render(request,'communication/messages.html',{'chatlist': chatlist,'form': form})

@login_required
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        queryset = CustomUser.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
        result = queryset.filter(fullname__contains=searched)
        return render(request,'communication/search.html',{'searched': searched,'people': result})
    else:
        return render(request,'communication/search.html',{})
