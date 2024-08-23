from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chat/<int:id>/', views.chat, name="chat"),
    path('chat/<int:id>/send-message/', views.send_message, name="send-message"),
    path('chat/<int:id>/get-messages/', views.get_messages, name="get-messages"),
]
