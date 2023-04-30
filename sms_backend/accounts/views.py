from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Invoices, Receipt
from .serializers import InvoicesSerializers, ReceiptSerializer
from rest_framework.response import Response

# Create your views here.


class InvoicesApiViewset(viewsets.ModelViewSet):
    serializer_class = InvoicesSerializers
    # GET

    def list(self, request):
        invoices = Invoices.objects.all()
        serializer = InvoicesSerializers(invoices, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        serializer = InvoicesSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReceiptApiViewset(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer
    # GET

    def list(self, request):
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    # POST
    def create(self, request):
        serializer = ReceiptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
