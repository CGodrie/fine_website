from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ContactForm

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f"Message de {name} via le formulaire de contact",
                message,
                email,
                ['clemgod5@gmail.com'],  # charger dynamiquement 
                fail_silently=False,
            )
            
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'main/contact_success.html')