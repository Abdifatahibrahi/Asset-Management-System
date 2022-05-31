from django.urls import path
from . import views

urlpatterns=[
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='admin_login'),
    path('admin_logout/', views.Logout_admin, name='admin_logout'),
    path('index/', views.index, name='dashboard'),

    path('view_furnitures/', views.view_furniture, name='view_furnitures'),
    path('add_furnitures/', views.add_furniture, name='add_furnitures'),
    path('delete_furnitures(?P<int:did>/)', views.delete_furniture, name='delete_furniture'),

    # path('view_patient/', views.view_patient, name='view_patient'),
    # path('add_patient/', views.add_patient, name='add_patient'),
    # path('delete_patient(?P<int:pid>/)', views.delete_patient, name='delete_patient'),

    # path('view_appointment/', views.view_Appointment, name='view_appointment'),
    # path('add_appointment/', views.add_appointment, name='add_appointment'),
    # path('delete_appointment(?P<int:aid>/)', views.delete_Appointment, name='delete_appointment'),
]