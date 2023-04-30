from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# create a model for the student

# student user profile


class StudentUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='student_users')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='student_users',
        blank=True,
    )
# Student model


class Student(models.Model):
    student_user = models.OneToOneField(
        StudentUser, on_delete=models.CASCADE)
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, default="Male")
    reg_no = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    admission_date = models.DateField(default=timezone.now)
    phone_no_validator = RegexValidator(regex="^[0-9]{10,15}$",
                                        message="Entered mobile number isn't in a right format!"
                                        )
    mobile_number = models.CharField(
        validators=[phone_no_validator], max_length=13, blank=True
    )
    parent_name = models.CharField(max_length=50)
    parent_mobile_number = models.CharField(
        validators=[phone_no_validator], max_length=13, blank=True
    )
    address = models.TextField(blank=True)


# create a autogenerate reg_no for the student
@receiver(pre_save, sender=Student)
def create_student_reg_no(sender, instance, **kwargs):
    if not instance.reg_no:
        last_student = sender.objects.last()
        if not last_student:
            new_reg_no = 'ST0001'
        else:
            last_reg_no = int(last_student.reg_no[2:])
            new_reg_no = 'ST' + '{0:04d}'.format(last_reg_no + 1)
        instance.reg_no = new_reg_no
