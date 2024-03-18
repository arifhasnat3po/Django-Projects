from django.urls import path
from first_app import views

urlpatterns = [
    path('first_app', views.index, name='index'),
]