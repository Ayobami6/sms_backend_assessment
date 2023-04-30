from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to='staffs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

# create staff custom user model


class StaffUser(AbstractUser):
    is_staff = models.BooleanField(default=True)

# create staff profile model


class StaffProfile(models.Model):
    staff_user = models.OneToOneField(
        StaffUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to='staffs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)
