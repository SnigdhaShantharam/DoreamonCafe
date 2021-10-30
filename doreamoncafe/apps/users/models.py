from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.meta_app.models import MyBaseModel


class DoreamonCafeUser(AbstractBaseUser, PermissionsMixin, MyBaseModel):
    mobile_number = PhoneNumberField(unique=True)

    email = models.EmailField(blank=True, null=True)

    first_name = models.CharField(max_length=200,
                                  blank=False,
                                  null=False,
                                  default='user')

    last_name = models.CharField(max_length=200,
                                 blank=True,
                                 null=True)

    address = models.CharField(max_length=255,
                                 blank=True,
                                 null=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'mobile_number'
