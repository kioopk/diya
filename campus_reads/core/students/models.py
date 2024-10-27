from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, enrollmentno, password=None, **extra_fields):
        if not enrollmentno:
            raise ValueError('The Enrollment Number must be set')
        
        if not extra_fields.get('fullname'):
            raise ValueError('The Fullname must be set')
        
        user = self.model(enrollmentno=enrollmentno, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, enrollmentno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(enrollmentno, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    enrollmentno = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='customuser',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'enrollmentno'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.enrollmentno

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
