from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Fitness')
    image_url = models.CharField(max_length=255) # Statik fayl yolu
    meta_info = models.CharField(max_length=100) # Çəki, ölçü və s.
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"
