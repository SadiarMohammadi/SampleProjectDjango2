from django.contrib import admin
from django.urls import path, include

from employee import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.show),
    path('emp/', views.emp, name='emp'),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
