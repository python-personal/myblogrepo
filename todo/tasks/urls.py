from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='list'),
    path('update/<str:id>/', views.update,name='update'),
    path('delete/<str:id>/', views.delete,name='delete'),
]
