from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .models import CarouselImage, NextConference, ActOfTheDays, CAFile
from django.contrib.auth.models import User
from users.models import Profile
import os

@receiver(post_delete, sender=CarouselImage)
def delete_image_file(sender, instance, **kwargs):
        # Supprimer le fichier image si il existe
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            try:
                os.remove(image_path)
                print(f"Fichier image supprimé : {image_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier image : {e}")


@receiver(post_delete, sender=NextConference)
def delete_programme(sender, instance, **kwargs):
    """
    Suppression des fichiers associés (PDF et image) lorsque l'instance du modèle est supprimée.
    """
    if instance.programme:
        pdf_path = instance.programme.path
        if os.path.isfile(pdf_path):
            try:
                os.remove(pdf_path)
                print(f"Fichier PDF supprimé : {pdf_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier PDF : {e}")

    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            try:
                os.remove(image_path)
                print(f"Fichier image supprimé : {image_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier image : {e}")


@receiver(post_delete, sender=ActOfTheDays)
def delete_act_files(sender, instance, **kwargs):
    """
    Suppression du fichier associé lorsque l'instance du modèle ActOfTheDays est supprimée.
    """
    # Supprimer le fichier si il existe
    if instance.file:
        file_path = instance.file.path
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Fichier supprimé : {file_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier : {e}")

@receiver(post_delete, sender=CAFile)
def delete_ca_file(sender, instance, **kwargs):
    """
    Suppression du fichier associé lorsque l'instance du modèle ActOfTheDays est supprimée.
    """
    # Supprimer le fichier si il existe
    if instance.file:
        file_path = instance.file.path
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Fichier supprimé : {file_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier : {e}")

@receiver(user_logged_in)
def force_password_change(sender, request, user, **kwargs):
    try:
        if user.profile.password_needs_change:  # Vérifie si le profil existe
            request.session['force_password_change'] = True
    except ObjectDoesNotExist:
        # Si le profil n'existe pas, ignore ou gère l'erreur
        pass
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, password_needs_change=True)

