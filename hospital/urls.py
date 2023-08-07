from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('nav', views.navigation, name='navigation'),
    path('login', views.login, name='login'),
    path('logout', views.logout_admin, name='logout_admin'),
    path('view_doctor', views.view_doctor, name='view_doctor'),
    path('add_doctor', views.add_doctor, name='add_doctor'),

]