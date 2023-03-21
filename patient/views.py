from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@api_view(['post'])
@login_required
def create(request):
    request.data['user']=request.user.id
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['get'])
def show(request, pk):
    patient = Patient.objects.get(id = pk)
    serializer = ShowPatientSerializer(patient, many=False)
    return Response(serializer.data, status=200)

@api_view(['put', 'patch'])
@login_required
def update(request):
    request.data['user']=request.user.id
    patient=request.user.patient
    serializer = PatientSerializer(patient,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['get'])
def index(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)