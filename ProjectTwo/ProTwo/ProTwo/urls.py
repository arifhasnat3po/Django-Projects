from django.contrib import admin
from django.urls import path
from AppTwo import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path (' ', include('AppTwo.urls')), # Include urls
    path('AppTwo ', views.help, name='help'),
]