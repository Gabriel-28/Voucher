from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Role(models.Model):
    """
    Represents different roles in the system.
    Attributes:
    - role (str): The name of the role.
    """
    role = models.CharField(max_length=100)

class CustomUserManager(BaseUserManager):
    """Custom manager for the CustomUser model.
    This manager provides methods to create users and superusers with specific roles.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates a regular user with the specified
        email, password, role, and additional fields.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Creates a superuser with the given email,password and with admin privileges. """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(email, password, **extra_fields)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model representing system users.
    """
    email = models.EmailField(('email_address'), unique=True)
    # Add your custom fields here
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    # Add more fields as needed
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return str(self.email)


class Voucher(models.Model):
    code = models.CharField(max_length=255)
    max_redemptions = models.IntegerField()
    remaining_redemptions = models.IntegerField()
    expiration_time = models.DateTimeField()
    redemption_type = models.IntegerField()
