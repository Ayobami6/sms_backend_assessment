from django.db import models
from students.models import Student

# Create your models here.


class Invoices(models.Model):
    semester_choices = [("1st", 1), ("2nd", 2)]
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.student_name


class Receipt(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE, null=True)
    amount_paid = models.IntegerField(default=0)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice.student_id.student_name
