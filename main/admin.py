from django.contrib import admin
from .models import CarouselImage, NextConference, ActOfTheDays, LinksCategories, UsefullLinks, LearningResources, CAFile

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

class NextConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'inscription_open']

class ActOfTheDaysAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']

class LinksCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']

class UsefullLinksAdmin(admin.ModelAdmin):
    list_display = ['title']
    
class LearningResourcesAdmin(admin.ModelAdmin):
    list_display = ['title']
    
class CAFilesAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(NextConference, NextConferenceAdmin)
admin.site.register(ActOfTheDays, ActOfTheDaysAdmin)
admin.site.register(LinksCategories, LinksCategoriesAdmin)
admin.site.register(UsefullLinks, UsefullLinksAdmin)
admin.site.register(LearningResources, LearningResourcesAdmin)
admin.site.register(CAFile, CAFilesAdmin)