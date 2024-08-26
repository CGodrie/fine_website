from django.db import models

class CarouselImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='carousel_images/')
    order = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage des images")
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Image {self.id}"

class NextConference(models.Model):
    title = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    programme = models.FileField(upload_to='conferences/programmes/', blank=True, null=True)
    image = models.ImageField(upload_to='conferences/images/', default='conferences/images/image002.jpg')
    link_form = models.CharField(max_length=100, blank=True)
    inscription_open = models.BooleanField(default=False)

    def __str__(self):
        return self.title or f"Conference {self.id}"
