from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.core.exceptions import ValidationError


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
    image = models.ImageField(upload_to='conferences/images/', default='conferences/images/default.png')
    link_form = models.CharField(max_length=100, blank=True)
    inscription_open = models.BooleanField(default=False)

    def __str__(self):
        return self.title or f"Conference {self.id}"
    
def upload_to(instance, filename):
    year = instance.year
    return f'acts/files/{year}/{filename}'

class ActOfTheDays(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_to)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2011),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        default=datetime.datetime.now().year
    )

class LinksCategories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class UsefullLinks(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=False)
    category = models.ForeignKey(LinksCategories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class LearningResources(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)  # Autoriser le champ URL à être vide
    file = models.FileField(upload_to='learning_ressources/', blank=True, null=True)

    def clean(self):
        if self.url and self.file:
            raise ValidationError("Vous ne pouvez pas remplir à la fois le champ URL et le champ fichier.")
        if not self.url and not self.file:
            raise ValidationError("Vous devez remplir soit le champ URL, soit le champ fichier.")

    def __str__(self):
        return self.title


class CAFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='ca_files/')
    
    def __str__(self):
        return self.title
    
class AGFile(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    file = models.FileField(upload_to='ag_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

class Meeting(models.Model):
    title = models.CharField(max_length=255, default="Réunion")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Réunion du {self.date} - {self.location}"
    


