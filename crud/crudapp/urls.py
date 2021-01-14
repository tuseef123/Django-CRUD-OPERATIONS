from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('record',views.records,name="record"),
    path('show/',views.show,name="show"),
    path('edit/<int:pk>/',views.update,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
]