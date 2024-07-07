from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    # def get_absolute_url(self):
    #     return reverse('products', kwargs={'pk': self.pk})
    
    def __str__(self) -> str:
        return f"{self.id}-{self.title} :{self.likes}"
