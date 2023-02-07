from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response 
from .models import Schedule
from .serializers import *

@api_view(['post'])
@login_required
def create(request):
    request.data['doctor']=request.user.doctor.id
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['get'])
def show(request, pk):
    schedule = Schedule.objects.get(id = pk)
    serializer = ShowScheduleSerializer(schedule, many=False)
    return Response(serializer.data, status=200)