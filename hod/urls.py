from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("hod_register/", views.hod_register),
]
