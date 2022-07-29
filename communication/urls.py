from django.urls import path
from .views import PostDetailView,PostUpdateView,PostDeleteView,PostCreateView, postdetail, postlist, messageslist,search

urlpatterns = [
    path('post/<int:pk>/', postdetail,name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/<int:courseid>', PostCreateView.as_view(),name='post-create'),
    path('post/list/<int:courseid>/',postlist,name='post-list'),
    path('messages/<int:personid>/',messageslist,name='chatlist'),
    path('search/',search,name='search')
]