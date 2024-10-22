from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.greeting, name='about'),
    path('test/', views.test, name='test'),

]