from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = [
        ('attendee', 'attendee'),
        ('admin', 'admin'),
        ('superAdmin', 'superAdmin'),
    ]
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full name"), max_length=150, blank=True)
    password = models.CharField(_("password"), max_length=128)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='attendee')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    google_id = models.CharField(max_length=100, blank=True, null=True)
    facebook_id = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['email','full_name', 'password'], 

    objects = CustomUserManager()

    def __str__(self):
        return self.email
