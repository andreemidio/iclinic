import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs['email']
        email = self.normalize_email(email)
        password = kwargs['password']
        kwargs.pop('password')

        if not email:
            raise ValueError('Necessário um email válido')

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    cellphone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255)
    reset_password = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email

    @property
    def ativo_human(self):
        return 'Sim' if self.is_active else 'Não'

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
