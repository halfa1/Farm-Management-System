from django.db import models

# Create your models here.

class FarmBlock(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='blocks/')

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=100)
    qualifications = models.TextField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    allocated_block = models.ForeignKey(FarmBlock, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
