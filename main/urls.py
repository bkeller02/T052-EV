from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-portal/admin_panel', views.admin_panel, name='admin_panel'),
    path('admin-portal/contact_support', views.contact_support, name='contact_support'),
    path('admin-portal/contact_submissions', views.contact_submissions, name='contact_submissions'),
    path('admin-portal/dashboard', views.dashboard, name='dashboard'),
    path('admin-portal/registered_users', views.registered_users, name='registered_users'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('data', views.turbine_data_page, name='data'),
    path('data/turbine1', views.turbine1, name='turbine1'),
    path('data/turbine2', views.turbine2, name='turbine2'),
    path('data/turbine3', views.turbine3, name='turbine3'),
    path('data/turbine4', views.turbine4, name='turbine4'),
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path("register", views.admin_register, name="register"),
]
