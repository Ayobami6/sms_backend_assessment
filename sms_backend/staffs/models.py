from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# create staff custom user model

# staff user profile


class StaffUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='staff_users')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='staff_users',
        blank=True,
    )


class Staffs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to='staffs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)
