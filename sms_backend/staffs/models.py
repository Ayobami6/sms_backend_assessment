from django.db import models

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
