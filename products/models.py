from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    price_per_quantity = models.DecimalField(max_digits=7, decimal_places=2)
    planting_date = models.DateField(null=True, blank=True)
    harvesting_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
