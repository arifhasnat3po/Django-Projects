from django.contrib import admin
from django.urls import path
from basicapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name = 'index'),
    path('formpage/', views.form_page, name="FormPage"), 
]
