# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .supabase_client import supabase
from .forms import VideoForm
from .models import Video
# from multimodal 

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
            return render(request, 'myapp/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'myapp/login.html')
    
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
            return render(request, 'myapp/login2.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'myapp/ogin2.html')
    
def my_supabase_view(request):
    # Fetch data from Supabase
    data = supabase.table("test_1").select("*").execute()

    # Process the data as needed, and prepare it for the template
    context = {
        'data': data.data if data.data else []  # Ensuring data exists
    }

    # Render the template with the data
    return render(request, 'myapp/your_template.html', context)

def video_list(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    videos = Video.objects.all()  # Fetch all video objects from the database
    time_points = [('Intro', 10, 30), ('Middle', 30, 45), ('End', 45, 47)]
    videos_exist = videos.exists()
    return render(request, 'myapp/video_list.html', {'videos': videos, 'time_points': time_points, 'form': form, 'videos_exist': videos_exist})

def delete_video(request, video_id):
    if request.method == 'POST':  # Ensure the request method is POST
        video = Video.objects.get(id=video_id)  # Get the video to delete
        video.delete()  # Delete the video
        return redirect('video_list')  # Redirect to the video list page