from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Pour ne pas déconnecter l'utilisateur
            user.profile.password_needs_change = False  # Met à jour l'état
            user.profile.save()
            messages.success(request, f'Votre mot de passe a bien été modifié')
            return redirect('home')  # Redirige vers une page de succès
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change-password.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Indique le bon chemin du template

    def get_success_url(self):
        if self.request.session.get('force_password_change'):
            return '/change-password/'  # Redirige vers la page de changement de mot de passe
        return super().get_success_url()
