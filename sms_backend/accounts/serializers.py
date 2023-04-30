from rest_framework import serializers
from .models import Invoices, Receipt


class InvoicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = "__all__"


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = "__all__"
