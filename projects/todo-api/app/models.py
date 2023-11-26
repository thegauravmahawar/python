from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        indexes = [
            models.Index(fields=['email', 'password'], name='user_email_password_idx')
        ]

    def __str__(self):
        return self.email
