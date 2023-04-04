"""Library_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name= 'home_page'),
    path('show-book/', views.show_book, name= 'active_book'),
    path('update-book/<int:pk>/', views.update_book, name= 'update_book'),
    path('hard-delete-book/<int:pk>/', views.hard_delete_book, name= 'hard_delete_book'),
    path('soft-delete-book/<int:pk>/', views.soft_delete_book, name= 'soft_delete_book'),
    path('restore-book/<int:pk>/', views.restore_book, name= 'restore_book'),
    
    path('inactive-book/', views.inactive_book, name= 'inactive_book'),




]
