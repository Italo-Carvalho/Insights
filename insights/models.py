from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("O e-mail deve ser definido"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("O superusuário deve está is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("O superusuário deve está is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("E-mail", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = CustomUserManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.email


class Tags(models.Model):
    name = models.CharField(max_length=80, verbose_name=_("Nome da Tag"))

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Card(models.Model):
    tags = models.ManyToManyField(Tags, related_name="card", blank=True)
    texto = models.TextField(verbose_name=_("Texto"), max_length=400)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.texto
