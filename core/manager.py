from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # define method for access all queryset
    def get_archive(self):
        return super().get_queryset()

    # define method for access all active query
    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define deactivate item
    def get_deactivate_list(self):
        return self.get_queryset().filter(is_active=False)


class UserManager(BaseUserManager):
    def create_user(self, phone, email, full_name, password):
        if not phone:
            raise ValueError(_('user must have Phone Number'))
        if not email:
            raise ValueError(_('user must have Email'))

        user = self.model(phone=phone, email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, full_name, password):
        user = self.create_user(phone, email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
