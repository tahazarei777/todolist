from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleType(models.TextChoices):
    ADMIN = "admin", "Admin"
    USER = "user", "User"


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=RoleType.choices,
        default=RoleType.USER,
    )
    phone = models.CharField(max_length=11)
    address = models.TextField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )