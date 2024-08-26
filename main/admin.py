from django.contrib import admin
from .models import CarouselImage, NextConference

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

class NextConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'inscription_open']

admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(NextConference, NextConferenceAdmin)