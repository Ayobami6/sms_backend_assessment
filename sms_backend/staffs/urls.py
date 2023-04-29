from django.contrib import admin
from django.urls import path
from .views import StaffViewSet

urlpatterns = [
    path('staffs/',
         StaffViewSet.as_view({'get': 'list', 'post': 'create'})),
]
