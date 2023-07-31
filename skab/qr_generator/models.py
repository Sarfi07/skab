from django.db import models

from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    pass

class Categorie(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name}"


class Brand(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name}"

class Product(models.Model):
    # stock_code, gender age-group, brand, rate, quantity, shade
    product_name = models.CharField(max_length=48)
    description = models.CharField(max_length=128)
    sku = models.CharField(max_length=16)
    price = models.PositiveIntegerField()
    # quantity_in_stock = models.PositiveIntegerField()
    size = models.CharField(max_length=8, null=True, blank=True)
    color = models.CharField(max_length=16, blank=True, null=True)
    material = models.CharField(max_length=32)
    imageURL = models.URLField()
    categoryId = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    brandId = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.sku}: {self.product_name} having price Rs. {self.price}"



class Stock(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_in = models.IntegerField(help_text="Qunatity received")
    stock_out = models.IntegerField(help_text="Quantity sold or removed from stock")
    stock_date = models.DateField(default=datetime.date.today, help_text="date of stock movement")
    stock_type = models.CharField(max_length=32, help_text="e.g., Purchase, Sale, Return, etc.")

class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.name}, {self.email}"
    


class Sales(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    saleDate = models.DateField(default=datetime.date.today)
    total_amount = models.IntegerField()

class Sale_item(models.Model):
    sale_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    subtotal = models.IntegerField()


class qr(models.Model):
    qr_code_data = models.CharField(max_length=64, null=False, blank=False)
    qr_image = models.BinaryField(null=False, blank=False)
    creation_date = models.DateField(default=datetime.date.today, null=False, blank=False)
    description = models.CharField(max_length=128)
    


