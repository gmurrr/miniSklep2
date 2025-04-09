from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_price = models.CharField(max_length=64)

    def __str__(self):
        return "Nazwa produktu: {} Cena produktu: {}".format(self.product_name, self.product_price)
# Create your models here.