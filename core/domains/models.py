from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Registrar(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Domain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="domains")
    name = models.CharField(max_length=255, unique=True)
    registrar = models.ForeignKey(Registrar, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class WHOISContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="whois_contacts")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
