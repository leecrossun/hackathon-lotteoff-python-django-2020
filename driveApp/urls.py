from django.urls import path
from . import views

urlpatterns = [
    path('driveThru/', views.driveThru, name='driveThru'),
    path('loginWarning/', views.loginWarning, name='loginWarning'),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]