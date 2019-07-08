# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from rest_framework import generics
from .serializer import CustomerSerializer, FamilySerializer
# Create your views here.


class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UpdateCustomerView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeleteCustomerView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FamilyView(generics.CreateAPIView):
    queryset = CustomerFamily.objects.all()
    serializer_class = FamilySerializer

class UpdateFamilyView(generics.UpdateAPIView):
    queryset = CustomerFamily.objects.all()
    serializer_class = FamilySerializer

class DeleteFamilyView(generics.DestroyAPIView):
    queryset = CustomerFamily.objects.all()
    serializer_class = FamilySerializer
