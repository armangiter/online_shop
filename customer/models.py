from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=13, unique=True, verbose_name=_('Phone'))
    full_name = models.CharField(max_length=255, verbose_name=_('Full Name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'), help_text=_('is user an active user'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Is Admin'), help_text=_('is user an admin'))

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'phone'

    objects = UserManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.phone} - {self.code} - {self.created}'


class Address(models.Model):
    city = models.CharField(max_length=40, null=True, blank=True)
    text = models.CharField(max_length=250)
    postal_code = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
