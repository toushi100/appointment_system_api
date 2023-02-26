from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from .models import Schedule, Appointment
from .serializers import *
from datetime import timedelta
from django.utils import timezone


@api_view(['post'])
@login_required
def create(request):
    doctor = request.user.doctor
    request.data['doctor']=doctor.id
    if doctor.status  != 'active':
        return Response({'error':'Doctor is not active'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['get'])
def show(request, pk):
    schedule = get_object_or_404(Schedule, id = pk)
    serializer = ShowScheduleSerializer(schedule, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view(['put','patch'])
@login_required
def reserve(request, pk):
    appointment = get_object_or_404(Appointment, id = pk)
    user = request.user
    if user.patient:
        request.data['patient']=user.patient.id
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['get'])
def list_available(request,doctor_id):
    appointments = Appointment.objects.filter(patient__isnull=True, start_time__gte=timezone.now(),
                                              schedule__doctor__id=doctor_id)
    serializer = ShowAppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['get'])
@login_required
def list_reserved(request):
    doctor_id = request.user.doctor.id
    appointments = Appointment.objects.filter(patient__isnull=False,schedule__doctor__id=doctor_id,
                                              start_time__range=[timezone.now()-timedelta(days = 7),
                                                                   timezone.now()+timedelta(days = 7)]
)
    serializer = ShowAppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)