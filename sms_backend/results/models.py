from django.db import models
from students.models import Student
from courses.models import Courses

# Create your models here.


class Result(models.Model):
    semester_choices = [("1st", 1), ("2nd", 2)]
    student_id = models.ForeignKey(
        Student, on_delete=models.DO_NOTHING, null=True)
    semester = models.CharField(max_length=50, choices=semester_choices)
    level = models.IntegerField(default=100)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    def __str__(self):
        return self.student_id.student_name
