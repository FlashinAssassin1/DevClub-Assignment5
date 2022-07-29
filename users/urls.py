from django.urls import include, path
from .views import CourseCreateView, register,profile,CourseListView,coursedetail,CourseUpdateView,CourseDeleteView,AdminCourseUpdateView,coursestudents
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('',CourseListView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/<int:pk>/',profile,name="profile"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path('course/<int:pk>/', coursedetail,name='course-detail'),
    path('course/new/', CourseCreateView.as_view(),name='course-create'),
    path('course/<int:pk>/admin-update/', AdminCourseUpdateView.as_view(),name='admin-course-update'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(),name='course-update'),
    path('post/<int:pk>/delete/', CourseDeleteView.as_view(),name='course-delete'),
    path('course/<int:pk>/students/',coursestudents,name='course-students'),
]