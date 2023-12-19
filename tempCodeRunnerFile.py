# key_manager_app/models.py
from django.db import models

class APIKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
