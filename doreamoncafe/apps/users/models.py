from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.meta_app.models import MyBaseModel

class UserManager(BaseUserManager):
    """
    Custom model manager

    Arguments:
        BaseUserManager -- To define a custom manager that extends BaseUserManager
                                providing two additional methods

    Raises:
        TypeError -- It raises if the password is not provided while creating the users.

    Returns:
        user_object -- This will override the default model manager and returns user object.
    """

    def create_user(self, mobile_number=None, password=None):
        if not mobile_number:
            raise TypeError('Users must have valid mobile number address.')

        user = self.model(mobile_number=mobile_number, password=password)
        user.set_password(password)
        # user.is_active = True     Default value is True
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password):
        if not mobile_number:
            raise TypeError('Users must have valid mobile number address.')
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(mobile_number=mobile_number, password=password)
        # user.is_active = True     Default value is already True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class DoreamonCafeUser(AbstractBaseUser, PermissionsMixin, MyBaseModel):
    mobile_number = models.CharField(max_length=10,unique=True)

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
    objects = UserManager()
