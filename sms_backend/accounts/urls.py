from django.contrib import admin
from django.urls import path
from .views import InvoicesApiViewset, ReceiptApiViewset


urlpatterns = [
    path('invoices/',
         InvoicesApiViewset.as_view({'get': 'list', 'post': 'create'})),
    path('receipts/',
         ReceiptApiViewset.as_view({'get': 'list', 'post': 'create'})),

]
