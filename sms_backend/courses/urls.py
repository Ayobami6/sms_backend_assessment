from django.contrib import admin
from django.urls import path
from .views import CoursesApiViewSet

urlpatterns = [
    path('courses/',
         CoursesApiViewSet.as_view({'get': 'list', 'post': 'create'})),
]
