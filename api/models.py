from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            name=name,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(
            name,
            email,
            password=password,
        )

        user.is_staff = True
        user.is_user = True
        user.is_patron = True
        user.is_moderator = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(max_length=255, unique=True)
    contact = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255, unique=True)
    joined = models.DateTimeField('date joined', default=timezone.now)

    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_user = models.BooleanField(default=True)
    is_patron = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def get_contact(self):
        return self.contact

    def __str__(self):
        return self.email
