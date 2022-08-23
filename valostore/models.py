from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField()
    server = models.CharField(max_length=10)
    slug = models.SlugField(default="-")
    last_online = models.DateTimeField(auto_now=True)


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    phone = models.IntegerField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
