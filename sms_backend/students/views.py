from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    # GET

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
