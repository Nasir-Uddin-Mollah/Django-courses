from django.shortcuts import render
from .import models, serializers
from rest_framework import viewsets
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer