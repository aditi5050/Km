# models.py

from django.db import models

class KeyPair(models.Model):
    keypair_id = models.CharField(max_length=255, unique=True)
    public_key = models.TextField()
    private_key = models.TextField()
    class Meta:
            app_label = 'km'

class Message(models.Model):
    size = models.IntegerField()
    recipient = models.CharField(max_length=255)
    keys = models.ManyToManyField(KeyPair, related_name='messages')
