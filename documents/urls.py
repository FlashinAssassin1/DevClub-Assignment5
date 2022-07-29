from django.urls import path
from documents.views import DocumentCreateView, DocumentUpdateView, DocumentDeleteView, DocumentDetailView, DocumentListView, documentlist

urlpatterns = [
    path('upload/<int:courseid>/',DocumentCreateView.as_view(),name='document-upload'),
    path('update/<int:courseid>/<int:pk>/',DocumentUpdateView.as_view(),name='document-update'),
    path('delete/<int:courseid>/<int:pk>/',DocumentDeleteView.as_view(),name='document-delete'),
    path('detail/<int:courseid>/<int:pk>/',DocumentDetailView.as_view(),name='document-detail'),
    path('list/<int:courseid>/',documentlist,name='document-list'),
]