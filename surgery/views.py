from rest_framework import status
from .models import Doctor, Surgery
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from .filters import SurgeryFilter


@api_view(['GET'])
def index_past(request):
    filters = request.data.get('filters', {})
    qs = Surgery.objects.filter(end_time__lt=timezone.now())
    past_surgeries = SurgeryFilter(filters, queryset=qs).qs
    serializer = ShowSurgerySerializer(past_surgeries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def index_upcoming(request):
    filters = request.data.get('filters', {})
    qs = Surgery.objects.filter(start_time__gt=timezone.now())
    upcoming_surgeries = SurgeryFilter(filters, queryset=qs).qs
    serializer =ShowSurgerySerializer(upcoming_surgeries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    if request.data.get('doctors'):
        request.data['doctors'].append(request.user.doctor.id)
    else:
        request.data['doctors'] = [request.user.doctor.id]
    serializers = SurgerySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)