from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.

class GFG(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # Add other fields as needed

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []