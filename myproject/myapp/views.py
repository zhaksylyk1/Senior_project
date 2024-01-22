# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .supabase_client import supabase

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def register_login_view(request):
    page = 'registration_login'

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request,"Username OR password does not exist")

    context = {'page': page}
    return render(request, 'registration_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('registration_login')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, "An error ocurred during registration")
            
    return render(request, 'registration_login.html', {'form': form})

@login_required(login_url='registration_login')
def login_view(request):
   
    return render(request, 'login.html')
    
@login_required(login_url='registration_login')    
def login_view2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page
        else:
            # Return an 'invalid login' error message
            return render(request, 'login2.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login2.html')
    
def my_supabase_view(request):
    # Fetch data from Supabase
    data = supabase.table("test_1").select("*").execute()

    # Process the data as needed, and prepare it for the template
    context = {
        'data': data.data if data.data else []  # Ensuring data exists
    }

    # Render the template with the data
    return render(request, 'your_template.html', context)


