from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('histoire', views.history, name="history"),
    path('objectifs', views.objectives, name="objectives"),
    path('ag-ca', views.agca, name="ag-ca"),
    path('contact', views.contact, name="contact"),
    path('evenements', views.events, name="events"),
    path('ca-zone-privée', views.caprivatezone, name="ca-private-zone"),

]
