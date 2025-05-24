from django.db import models

class User(models.Model):
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
