from django.contrib import admin
from django.urls import path
from .views import ResultApiView

urlpatterns = [
    path('results/', ResultApiView.as_view({'get': 'list', 'post': 'create'})),
]
