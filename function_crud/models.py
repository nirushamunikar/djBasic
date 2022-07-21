from django.db import models

# Create your models here.
class Laptops(models.Model):
    manufacturer = models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)
    gpu = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return (self.name)