from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CarsViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.Cars.objects.get(id=id)
            serializer = serializers.CarSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = models.Cars.objects.all()
        serializer = serializers.CarSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        item = models.Cars.objects.get(id=id)
        serializer = serializers.CarSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = models.Cars.objects.get(id=id)
        if item:
            item.delete()
            return Response({"status": "success", "data": "deleted"}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": "not found"}, status=status.HTTP_400_BAD_REQUEST)
            