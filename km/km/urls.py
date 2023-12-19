# urls.py

from django.urls import path
from .views import keypair_list, message_list, create_keypair, create_message

urlpatterns = [
    path('keypairs/', keypair_list, name='keypair_list'),
    path('messages/', message_list, name='message_list'),
    path('create_keypair/', create_keypair, name='create_keypair'),
    path('create_message/', create_message, name='create_message'),
]
