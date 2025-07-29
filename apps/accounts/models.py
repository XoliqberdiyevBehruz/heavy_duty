from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.shared.models import BaseModel
from apps.accounts.managers import CustomUserManager


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=13, unique=True, verbose_name=_('telefon raqam'))

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')