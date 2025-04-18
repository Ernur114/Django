import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin,
    Group,
    Permission,
)
from .validators import UsernameValidator, StrongPasswordValidator, AllowedEmailValidator

class ClientManager(BaseUserManager):
    def create_superuser(
        self, 
        username: str, 
        email: str,
        password: str,
    ) -> "Client":
        
        username_validator = UsernameValidator()
        email_validator = AllowedEmailValidator()
        password_validator = StrongPasswordValidator()

        username_validator(username)
        normalized_email = self.normalize_email(email)
        email_validator(normalized_email)
        password_validator(password)

        client = Client()
        client.email = self.normalize_email(email=email)
        client.username = username
        client.set_password(password)
        client.is_active = True
        client.is_staff = True
        client.is_superuser = True
        client.save()

        return client


class Client(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="никнейм",
        max_length=50,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name="",
        max_length=50,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name="",
        max_length=50,
        blank=True,
    )
    birthday = models.DateField(
        verbose_name="дата рождения",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="эл. почта",
        max_length=100,
        unique=True,
        db_index=True,
    )
    is_active = models.BooleanField(
        verbose_name="активный",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="сотрудник",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="администратор",
        default=False,
    )
    gender = models.CharField(
        verbose_name="пол",
        blank=True,
        null=True,
        max_length=10,
    )
    date_created = models.DateTimeField(
        verbose_name="дата создания",
        default=timezone.now,
    )
    groups = models.ManyToManyField(
        to=Group,
        verbose_name="группы",
        blank=True,
        related_name="clients_group",
    )
    user_permissions = models.ManyToManyField(
        to=Permission,
        verbose_name="разрешения",
        blank=True,
        related_name="clients_permissions",
    )

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"
    objects = ClientManager()

    class Meta:
        ordering = ("id",)
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return f"{self.username} | {self.email} | {self.date_created}"
