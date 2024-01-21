from django.urls import path
from . import views
from myapp.views import my_supabase_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login2/', views.login_view2, name='login2'),
    path('supabase-data/', my_supabase_view, name='supabase_data'),
]
