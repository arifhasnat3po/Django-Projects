from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
     path ('', include('first_app.urls')), # Include urls
]
