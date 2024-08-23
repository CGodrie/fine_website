from django.shortcuts import render
from .models import Discussion, Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, template_name='main/home.html')

def history(request):
    return render(request, template_name='main/history.html')
    
def objectives(request):
    return render(request, template_name='main/objectives.html')

def agca(request):
    return render(request, template_name='main/home.html')

def contact(request):
    return render(request, template_name='main/home.html')

def events(request):
    return render(request, template_name='main/home.html')

def caprivatezone(request):
    return render(request, template_name='main/home.html')