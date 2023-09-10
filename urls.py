"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_file_list, name='file_list'),
    path('create/', views.create_text_file, name='create_file'),
    path('edit/<int:pk>/', views.edit_text_file, name='edit_file'),
    path('view/<int:pk>/', views.view_text_file, name='view_file'),
]
