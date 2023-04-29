from django.db import models
from staffs.models import Staffs

# Create your models here.


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_description = models.TextField(blank=True)
    course_unit = models.IntegerField()
    course_status = models.BooleanField(default=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
