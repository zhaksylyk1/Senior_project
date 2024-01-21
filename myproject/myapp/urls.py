from django.urls import path
from . import views
from myapp.views import my_supabase_view

urlpatterns = [
<<<<<<< HEAD
    path('login/', views.login_view, name='login'),
    path('supabase-data/', my_supabase_view, name='supabase_data'),
=======
    path('login/', views.my_view, name='login'),
>>>>>>> 0f23b82 (Ali 1)
]
