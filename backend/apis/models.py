from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# custom User model as we want email based authentication system
# here we replace username and use email field which is unique and required

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is used
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the incomming email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERTYPES = (
        ('1','Admin'),
        ('2','Student'),
    )
#  two usertypes are defined , admin who can perform crud and student who can only perform read operation.
    UserType = models.CharField(choices = USERTYPES , max_length=20 , null=False , blank=False, default=USERTYPES[1][0])
    # by default ever new registration is student , however super user can change its usertype when required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['UserType']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
    
    def get_usertype(self):
        return self.UserType

#  A simple Book model for storing its information
class Book(models.Model):
    Name = models.CharField(max_length = 50)
    Author = models.CharField( max_length=50)
    Discription= models.CharField(max_length=100)

