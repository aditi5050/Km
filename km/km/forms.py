# forms.py

from django import forms
from .models import KeyPair, Message

class KeyPairForm(forms.ModelForm):
    class Meta:
        model = KeyPair
        fields = ['keypair_id', 'public_key', 'private_key']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['size', 'recipient', 'keys']
