from django import forms
from .models import ActOfTheDays

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse email'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tapez votre message', 'rows': 5})
    )

class ActsFilterForm(forms.Form):
    year = forms.ChoiceField(
        choices=[],
        required=False,
        label="Sélectionnez une année"
    )
    title = forms.CharField(
        required=False,
        label="Rechercher par titre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rechercher par titre'})
    )

    def __init__(self, *args, **kwargs):
        super(ActsFilterForm, self).__init__(*args, **kwargs)
        years = ActOfTheDays.objects.values_list('year', flat=True).distinct().order_by('-year')
        year_choices = [(year, year) for year in years]
        year_choices.insert(0, ('', 'Toutes les années'))
        self.fields['year'].choices = year_choices
