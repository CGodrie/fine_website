from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('histoire', views.history, name="history"),
    path('objectifs', views.objectives, name="objectives"),
    path('ag-ca', views.agca, name="ag-ca"),
    path('contact', views.contact, name="contact"),
    path('actes-des-journees', views.actcoftheday, name="acts-of-the-days"),
    path('ca-zone-privée', views.caprivatezone, name="ca-private-zone"),
    path('contact', views.contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)