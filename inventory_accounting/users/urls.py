from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.register_request, name='registration'),
    path('employees/', views.users_list, name='users_list'),
    path('employees/<int:user_id>', views.user_detail, name='user_detail'),
    path('employees/<int:user_id>/download', views.download_user_items, name='download-user-items'),
]
