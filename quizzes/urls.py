from django.urls import path
from .views import QuizCreateView, QuizListView, quizattempt,quizview

urlpatterns = [
    path('create/<int:courseid>',QuizCreateView.as_view(),name='quiz-create'),
    path('view/<int:courseid>/<int:pk>',quizview,name="quiz-view"),
    path('attempt/<int:courseid>/<int:pk>',quizattempt,name='quiz-attempt'),
    path('list/<int:courseid>/',QuizListView.as_view(),name='quiz-list'),
]