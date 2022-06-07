from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='admin_login'),
    path('admin_logout/', views.Logout_admin, name='admin_logout'),
    path('index/', views.index, name='dashboard'),

    path('view_furnitures/', views.view_furniture, name='view_furnitures'),
    path('add_furnitures/', views.add_furniture, name='add_furnitures'),
    path('delete_furniture(?P<s_no>/)', views.delete_furniture, name='delete_furniture'),
    
    
    path('view_vehicles/', views.view_vehicles, name='view_vehicles'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('delete_vehicle(?P<int:did>/)', views.delete_vehicle, name='delete_vehicle'),
    
    
    path('view_electronics/', views.view_electronics, name='view_electronics'),
    path('add_electronics/', views.add_Electronics, name='add_electronics'),
    path('delete_electronic(?P<int:did>/)', views.delete_Electronics, name='delete_electronic'),
    
    
    path('view_land/', views.view_land, name='view_land'),
    path('add_land/', views.add_Land, name='add_land'),
    path('delete_land(?P<int:did>/)', views.delete_land, name='delete_land'),
]