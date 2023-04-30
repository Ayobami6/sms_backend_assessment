from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Result
from rest_framework.response import Response
from .serializers import ResultSerializer

# Create your views here.


class ResultApiView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer

    # GET /api/results/
    def list(self, request):
        # query all results from database
        queryset = Result.objects.all()
        # jsonify the results
        serializer = ResultSerializer(queryset, many=True)
        # return the serialized results
        return Response(serializer.data)

    def create(self, request):
        # get data from request and jsonify it
        serializer = ResultSerializer(data=request.data)
        # check if data is valid
        serializer.is_valid(raise_exception=True)
        # if valid, save data to database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
