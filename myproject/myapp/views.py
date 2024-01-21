# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .supabase_client import supabase

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
def my_supabase_view(request):
    # Fetch data from Supabase
    data = supabase.table("test_1").select("*").execute()

    # Process the data as needed, and prepare it for the template
    context = {
        'data': data.data if data.data else []  # Ensuring data exists
    }

    # Render the template with the data
    return render(request, 'your_template.html', context)


