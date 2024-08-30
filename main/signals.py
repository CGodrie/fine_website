from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import CarouselImage, NextConference, ActOfTheDays
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
def delete_pdf_file(sender, instance, **kwargs):
    """
    Suppression des fichiers associés (PDF et image) lorsque l'instance du modèle est supprimée.
    """
    # Supprimer le fichier PDF si il existe
    if instance.pdf_file:
        pdf_path = instance.pdf_file.path
        if os.path.isfile(pdf_path):
            try:
                os.remove(pdf_path)
                print(f"Fichier PDF supprimé : {pdf_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier PDF : {e}")

    # Supprimer le fichier image si il existe
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



