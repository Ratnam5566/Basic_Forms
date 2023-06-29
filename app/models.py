from django.db import models

# Create your models here.

class User_Details(models.Model):
    Name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Name
