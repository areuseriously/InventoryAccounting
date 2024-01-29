from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>/download/', views.file_download, name='file_download'),
    path('files/<int:file_id>/delete/', views.file_delete, name='file_delete'),
    path('files/create/', views.file_create, name='file_create'),
]
