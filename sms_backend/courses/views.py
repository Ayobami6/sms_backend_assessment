from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Courses
from .serializers import CoursesSerializer
from rest_framework.response import Response
# Create your views here.


class CoursesApiViewSet(viewsets.ModelViewSet):
    # GET
    def list(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        serializer = CoursesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
