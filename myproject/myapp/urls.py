from django.urls import path
from . import views
from myapp.views import my_supabase_view

urlpatterns = [
    path('registration_login/', views.register_login_view, name='registration_login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),

    path('login/', views.login_view, name='login'),
    path('login2/', views.login_view2, name='login2'),
    path('supabase-data/', my_supabase_view, name='supabase_data'),
]
