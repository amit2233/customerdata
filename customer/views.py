# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CustomerSerializer, FamilySerializer

# Create your views here.


class CustomerView(APIView):
    def get(self, request):
        customers=Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'data':serializer.data})
    
    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data':serializer.data})
        
    def put(self, request, pk):
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data':serializer.data})

    def delete(self, request, pk):
        customer = Customer.objects.get(id=pk).delete()
        return Response({'status':'sucesss'})


class FamilyView(APIView):
    def get(self, request):
        family=CustomerFamily.objects.all()
        serializer = FamilySerializer(family, many=True)
        return Response({'data':serializer.data})
    
    def post(self, request):
        serializer = FamilySerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data':serializer.data})
        
    def put(self, request, pk):
        family = CustomerFamily.objects.get(id=pk)
        serializer = FamilySerializer(instance=family, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data':serializer.data})

    def delete(self, request, pk):
        family = CustomerFamily.objects.get(id=pk).delete()
        return Response({'status':'sucesss'})
