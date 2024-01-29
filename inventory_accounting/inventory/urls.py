from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.item_list, name='item_list'),
    path('inventory/item/<int:item_id>', views.item_detail, name='item_detail'),
    path('inventory/item/create/', views.item_create, name='item_create'),
    path('inventory/item/<int:item_id>/edit', views.item_edit, name='item_edit'),
    path('inventory/item/<int:item_id>/delete', views.item_delete, name='item_delete'),
    path('inventory/<int:user_id>/download', views.download_items, name='download-items'),
]
