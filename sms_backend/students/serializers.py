from rest_framework import serializers
from .models import Student

# For restapi


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
