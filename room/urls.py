from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('add/', views.add_room, name='add_room'),
    path('<slug:slug>/', views.room, name='room'),
]