from rest_framework import serializers
from .models import Staffs


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'
