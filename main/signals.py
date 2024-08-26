from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import CarouselImage, NextConference
import os

@receiver(post_delete, sender=CarouselImage)
def delete_image_file(sender, instance, **kwargs):
    """
    Suppression du fichier associé à l'image lorsque l'instance du modèle est supprimée.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=NextConference)
def delete_pdf_file(sender, instance, **kwargs):
    """
    Suppression du fichier PDF associé lorsque l'instance du modèle est supprimée.
    """
    if instance.pdf_file:
        if os.path.isfile(instance.pdf_file.path):
            os.remove(instance.pdf_file.path)
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

