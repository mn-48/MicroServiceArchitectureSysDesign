from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

 