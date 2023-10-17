from django.shortcuts import render, redirect
from .models import disney

# Create your views here.
def home(request):
    kids = disney.objects.all()
    return render(request, 'home.html', {'kids': kids})


def add_channel(request):
    if request.method == "GET":
        return render(request, 'add.html')
    else:
        disney (
            channel = request.POST.get('cnl'),
            cartoon = request.POST.get('crtn'),
            character = request.POST.get('chrt'),
            time = request.POST.get('time'),
        ) .save()
        return render(request, 'add.html')
    
    