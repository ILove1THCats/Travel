from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Location
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import LocationForm, RegisterForm

def index(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    locations = Location.objects.all()
    if query:
        locations = Location.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        locations = Location.objects.all()
    if category:
        locations = Location.objects.filter(category=category)
    context = {'locations': locations}
    return render(request, 'mapapp/index.html', context)

def get_locations(request):
    locations = Location.objects.all()
    data = [{'id': loc.id, 'name': loc.name, 'latitude': loc.latitude, 'longitude': loc.longitude, 'description': loc.description} for loc in locations]
    return JsonResponse(data, safe=False)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Đăng nhập người dùng sau khi đăng ký
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'mapapp/register.html', {'form': form})

@login_required
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longtitude = request.POST.get('longtitude')
        description = request.POST.get('description')
        location = Location(name=name, latitude=latitude, longitude=longtitude, description=description)
        location.save()
        return redirect('/')
    
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            return redirect('/')
    else:
        form = LocationForm()
    context = {'form': form, 'locations': Location.objects.all()}
    return render(request, 'mapapp/index.html')