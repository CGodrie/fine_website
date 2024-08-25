from django import forms

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
