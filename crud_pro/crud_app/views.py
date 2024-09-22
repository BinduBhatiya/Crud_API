from django.shortcuts import render
from rest_framework.response import Response
from .models import studentmodel
from .serializers import studentserializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class CrudApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = studentmodel.objects.get(id=id)
            serializer = studentserializer(stu)
            return Response(serializer.data)
        
        stu = studentmodel.objects.all()
        serializer = studentserializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Data Created sucessfully.'
            }, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = studentmodel.objects.get(id=id)
        serializer = studentserializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'complete Data updated.'
            }, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = studentmodel.objects.get(id=id)
        serializer = studentserializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Partial Data Updated.'
            })
        return Response(
            serializer.errors
            )
    
    def delete(self, request, pk, format=None):
        id = pk
        stu = studentmodel.objects.get(id=id)
        stu.delete()
        return Response({
                'msg':'Data deleted sucessfully.'
            })


