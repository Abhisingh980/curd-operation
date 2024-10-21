from django.urls import path

from .views import *

urlpatterns = [
    path('', view_record, name='view'),
    path('home', home, name='home'),
    path('register/', register, name='register'),
    path('login/', my_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('create_record/', create_record, name='add'),
    path('update_record/<int:pk>/', update_record, name='update'),
    path('delete_record/<int:pk>/', delete_record, name='delete'),
]
