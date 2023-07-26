from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('contactus',views.contctus, name="contactus"),
    path('career-page',views.career, name="career"),
    path('level-manufacturing',views.level_manufacturing, name="level-manufacturing")
]