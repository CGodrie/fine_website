from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm, ActsFilterForm
from django.shortcuts import render
from .models import CarouselImage, NextConference, ActOfTheDays, UsefullLinks, LearningResources, CAFile
from collections import defaultdict
from django.contrib.auth.decorators import login_required

def group_images(images, n):
    for i in range(0, len(images), n):
        yield images[i:i+n]

def home(request):
    images = CarouselImage.objects.all()
    image_groups = list(group_images(images, 3)) 
    next_conference = NextConference.objects.first()
    return render(request, 'main/home.html', {'images': images, 'image_groups': image_groups, 'next_conference': next_conference})

def history(request):
    return render(request, template_name='main/history.html')
    
def objectives(request):
    return render(request, template_name='main/objectives.html')

def agca(request):
    return render(request, template_name='main/ag-ca.html')

@login_required
def ca_private_zone(request):
    files = CAFile.objects.all()
    return render(request, template_name='main/ca-private-zone.html', context={'files': files})

def actc_of_the_day(request):
    form = ActsFilterForm(request.GET or None)
    acts = ActOfTheDays.objects.all()

    selected_year = None
    search_title = form.cleaned_data.get('title', '') if form.is_valid() else request.GET.get('title', '')

    sort_order = request.GET.get('sort', 'desc')
    if sort_order == 'asc':
        acts = acts.order_by('year')
    else:
        acts = acts.order_by('-year')

    if form.is_valid():
        selected_year = form.cleaned_data.get('year')
        if selected_year:
            acts = acts.filter(year=selected_year)

    if search_title:
        acts = acts.filter(title__icontains=search_title)

    acts_by_year = defaultdict(list)
    for act in acts:
        acts_by_year[act.year].append(act)

    acts_by_year = dict(acts_by_year)

    # Renvoyer les données au template
    return render(request, 'main/acts.html', {
        'form': form,
        'acts_by_year': acts_by_year,
        'selected_year': selected_year,
        'search_title': search_title,
        'sort_order': sort_order
    })

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

def links(request):
    links = UsefullLinks.objects.all()

    links_by_cat = defaultdict(list)
    for link in links:
        links_by_cat[link.category].append(link)

    links_by_cat = dict(links_by_cat)

    # Renvoyer les données au template
    return render(request, 'main/links.html', {
        'links_by_cat': links_by_cat,
    })

def learning_ressources(request):
    learning_ressources = LearningResources.objects.all()
    
    return render(request, 'main/learning-ressources.html', {
        'learning_ressources': learning_ressources,
    })