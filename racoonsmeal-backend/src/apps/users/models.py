from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    height_cm = models.FloatField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    activity_level = models.CharField(
        max_length=50,
        choices=[
            ("sedentary", "Sedentary"),
            ("lightly_active", "Lightly Active"),
            ("moderately_active", "Moderately Active"),
            ("very_active", "Very Active"),
        ],
        blank=True,
        null=True,
    )
    followers = models.ManyToManyField(User, related_name="following", blank=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username
