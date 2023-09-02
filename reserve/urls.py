from django.urls import path
from . import views

app_name = "reserve"

urlpatterns = [
    path('', views.index),
    path('csrf_token/', views.csrf_token, name="csrf_token"),
    path('delete_all/', views.delete_all, name="delete_all")
]
