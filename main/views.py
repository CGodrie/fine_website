from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm, YearFilterForm
from django.shortcuts import render
from .models import CarouselImage, NextConference, ActOfTheDays

def group_images(images, n):
    """Divise les images en groupes de n éléments."""
    for i in range(0, len(images), n):
        yield images[i:i+n]

def home(request):
    images = CarouselImage.objects.all()
    image_groups = list(group_images(images, 3)) 
    next_conference = NextConference.objects.first()
    return render(request, 'main/home.html', {'image_groups': image_groups, 'next_conference': next_conference})



def history(request):
    return render(request, template_name='main/history.html')
    
def objectives(request):
    return render(request, template_name='main/objectives.html')

def agca(request):
    return render(request, template_name='main/ag-ca.html')

def actcoftheday(request):
    form = YearFilterForm(request.GET or None)
    acts = ActOfTheDays.objects.all()

    # Gestion du tri
    sort_order = request.GET.get('sort', 'desc')  # 'desc' est la valeur par défaut
    if sort_order == 'asc':
        acts = acts.order_by('year')
    else:
        acts = acts.order_by('-year')

    # Application du filtre par année si le formulaire est valide
    if form.is_valid():
        selected_year = form.cleaned_data.get('year')
        if selected_year:
            acts = acts.filter(year=selected_year)
        else:
            selected_year = None  # Assurer que selected_year est défini même si aucun filtre n'est appliqué

    return render(request, 'main/acts.html', {
        'form': form,
        'acts': acts,
        'selected_year': selected_year,
        'sort_order': sort_order  # Ajouter le paramètre de tri à la context
    })


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
            messages.success(request, f'Merci pour votre message ! Nous reviendrons vers vous dès que possible.')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})
