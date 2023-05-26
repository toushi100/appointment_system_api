from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Service
from.serializers import *


@api_view(['GET'])
def show(request,pk):
    service = Service.objects.get(pk=pk)
    serializer = ShowServiceSerializer(service)
    return Response(serializer.data)

@api_view(['post'])
def create(request):
    request.data["patient"] = request.user.patient.id 
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['get'])
def index(request):
    services = Service.objects.all()
    serializer = ShowServiceSerializer(services, many=True)
    return Response(serializer.data)