from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom User model with extra fields
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username


# ✅ Book model required by ALX checker
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_create", "Can create book"),  # ✅ Checker requires
            ("can_delete", "Can delete book"),  # ✅ Checker requires
        ]
