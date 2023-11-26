from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    textMessage = models.TextField(max_length=10000)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email) + ", Date: " + str(self.creation_date.strftime('%B %d, %Y'))