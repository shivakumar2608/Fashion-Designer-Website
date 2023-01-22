import email
from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    reason = models.TextField()
    date = models.DateField()

    def __str__(self):
        name = self.firstname+ " " + self.lastname
        return name  
    


