from rest_framework import status
from .models import Doctor
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.
@api_view(['post'])
@login_required
def create(request):
    request.data['user']=request.user.id
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['get'])
def show(request, pk):
    doctor = Doctor.objects.get(id = pk)
    serializer = ShowDoctorSerializer(doctor, many=False)
    return Response(serializer.data, status=200)

@api_view(['put', 'patch'])
# @login_required
# @user_passes_test
def update(request):
    request.data['user']=request.user.id
    doctor=request.user.doctor
    serializer = DoctorSerializer(doctor,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)