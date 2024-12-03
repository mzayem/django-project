from django.urls import path
from . import views


urlpatterns = [
path('', views.greeting, name = 'greet'),
path('test/', views.test, name = 'test'),
path('index/', views.home, name = 'home'),
path('about-us/', views.contact, name = 'contact'),
path('media-files/', views.photos, name = 'gallary'),
path('create-product/', views.create_product, name = 'create_product'),
path('products/', views.fetch_all, name = 'fetch_all'),
path('delete/<int:pk>/', views.delete, name = 'delete'),
path('edit/<int:pk>/', views.edit_product, name = 'edit_product')


]