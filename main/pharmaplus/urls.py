from django.urls import path
from . import views


app_name = 'pharmaplus'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('contact/', views.contact, name = 'contact'),
]