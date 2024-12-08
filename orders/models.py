from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Order(models.Model):
    #refer to the custom usermodel after importing settings
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price_per_quantity

    def __str__(self):
        return f'Order by {self.user.username}'
