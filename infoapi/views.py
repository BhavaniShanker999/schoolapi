from django.shortcuts import render
from .serializers import *
from . models import *
from rest_framework import viewsets

# Create your views here.
class schoolview(viewsets.ModelViewSet):
    queryset=school_model.objects.all()
    serializer_class=school_serializer
    
class staffview(viewsets.ModelViewSet):
    queryset=staff_model.objects.all()
    serializer_class=staff_serializer
