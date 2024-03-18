from django.urls import path
from AppTwo import views

urlpatterns = [
    path('AppTwo ', views.help, name='help'),
]