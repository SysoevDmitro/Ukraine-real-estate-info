from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.IntegerField()
    postal_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.street} {self.number}"


class Realtor(AbstractUser):
    rating = models.DecimalField(max_digits=1, decimal_places=1, blank=True, null=True)

    class Meta:
        verbose_name = "realtor"
        verbose_name_plural = "realtors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("estate:realtor-detail", kwargs={"pk": self.pk})


class House(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, unique=True)
    price = models.IntegerField
    area = models.IntegerField()
    num_of_bedrooms = models.IntegerField(blank=True, null=True)
    num_of_floors = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    realtor = models.ManyToManyField(Realtor, related_name="house")

    def __str__(self):
        return f"{self.price}, {str(self.owner)}"


