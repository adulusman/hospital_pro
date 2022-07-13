from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.home,name='home'),
    path('department',views.department,name='department'),
    path('booking',views.booking,name='booking'),
    path('doctor',views.doctor,name='doctor'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]