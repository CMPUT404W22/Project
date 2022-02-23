from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class MyUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, is_staff=True, is_superuser=True, **extra_fields)


class Author(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=150, blank=False, null=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False, null=False)
    profile_header = models.TextField(_('profile header'), max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(blank=False, null=False, default=True)
    is_staff = models.BooleanField(blank=False, null=False, default=False)
    is_superuser = models.BooleanField(blank=False, null=False, default=False)

    USERNAME_FIELD = "username"

    objects = MyUserManager()

    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # created = not self.pk
        super().save(*args, **kwargs)
