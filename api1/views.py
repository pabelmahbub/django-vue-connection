from django.shortcuts import render
from rest_framework import viewsets
from .seralizers import PlanSerializers
from .models import Plan
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView 
# Create your views here.


class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers    