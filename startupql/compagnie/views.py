from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def employe(request, pk):
    data = {
        'pk':pk
    }
    return render(request, 'employe.html', data)
