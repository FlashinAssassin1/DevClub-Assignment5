from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from quizzes.forms import AddQuestionForm, CreateQuizForm
from users.models import Course
from .models import Question, Quiz, QuizAttempt
from django.contrib.auth.decorators import user_passes_test


def quizattempt(request, courseid, pk):
    quiz = Quiz.objects.filter(pk=pk).first()
    if request.method == 'POST':
        questions = Question.objects.filter(quiz=quiz)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += q.marks
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += q.marks
                correct += 1
            else:
                wrong += 1
        percent = score/(total) * 100
        timetaken = request.POST.get('timer')

        attempt = QuizAttempt(score=score, percentage=percent, time_taken=timetaken, correct_answers=correct,
                              incorrect_answers=wrong, total_marks=total, student=request.user, quiz=quiz)
        attempt.save()

        return redirect('quiz-view', courseid=courseid, pk=pk)

    else:
        questions = Question.objects.filter(quiz=quiz)
        time = timezone.now()
        try:
            attempt = quiz.quizattempt
            context = {
            'questions': questions,
            'quiz': quiz,
            'time': time,
            'attempted': True,
            }
        except:
            context = {
            'questions': questions,
            'quiz': quiz,
            'time': time,
            'attempted': False,
            }
        
        return render(request, 'quizzes/quizattempt.html', context)


def quizview(request, courseid, pk):
    quiz = Quiz.objects.filter(pk=pk).first()
    questions = Question.objects.filter(quiz=quiz)
    if (request.method == 'POST'):
        form = AddQuestionForm(request.POST)
        form.instance.quiz = quiz
        if(form.is_valid()):
            form.save()
            return redirect('quiz-view', courseid=courseid, pk=pk)
    else:
        form = AddQuestionForm()

    try:
        attempt = quiz.quizattempt
        minutes = attempt.time_taken // 60
        seconds = attempt.time_taken % 60
        context = {'form': form, 'attempt': attempt, 'quiz': quiz,
                   'questions': questions, 'minutes': minutes, 'seconds': seconds,'attempted': True}
    except:
        context = {'form': form, 'quiz': quiz, 'questions': questions,'attempted': False}
    return render(request, 'quizzes/quizview.html', context)


class QuizCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Quiz
    form_class = CreateQuizForm

    def test_func(self):
        if self.request.user.type == 2:
            return True
        return False

    def form_valid(self, form):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        form.instance.course = course
        return super().form_valid(form)


class QuizListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Quiz
    context_object_name = 'quizzes'
    ordering = ['-startafter_time']

    def test_func(self):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        if self.request.user in course.teachers.all() | course.students.all():
            return True
        return False

    def get_queryset(self):
        courseid = self.kwargs['courseid']
        course = Course.objects.filter(pk=courseid).first()
        return Quiz.objects.filter(course=course)
