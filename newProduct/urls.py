from django.urls import path
from . import views

urlpatterns = [
    path('newProduct/', views.newProduct, name='newProduct'),
    path('newProduct/<int:new_id>/', views.newDetail, name='newDetail'),
    path('newProduct/createApply/<int:new_id>/', views.createApply, name='createApply'),
    path('newProduct/deleteApply/<int:new_id>/<int:apply_id>/', views.deleteApply, name='deleteApply'),
]