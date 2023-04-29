from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Staffs
from .serializers import StaffSerializer
from rest_framework.response import Response

# Create your views here.


class StaffViewSet(viewsets.ModelViewSet):
    # GET
    def list(self, request):
        staffs = Staffs.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)
    # POST

    def create(self, request):
        serializer = StaffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
