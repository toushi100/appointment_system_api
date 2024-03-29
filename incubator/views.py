from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Incubator
from .serializers import *
from .filters import IncubatorFilter
from django.utils import timezone
from django.db.models import Q

@api_view(['POST'])
def create(request):
    serializers = IncubatorSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def reserved_incubators(request):
    filters = {
        "patient": request.GET.get('patient'),
        "incubator": request.GET.get('incubator'),
        "start_date__gte": request.GET.get('start_date__gte'),
    }
 
    icu = Incubator.objects.filter(Q(start_date__lte=timezone.now())& (Q(end_date=None)|Q(end_date__gte=timezone.now()))) 
    icu = IncubatorFilter(filters, queryset=icu).qs
    serializers = ShowIncubatorSerializer(icu, many=True)
    return Response(serializers.data)


@api_view(['PUT', 'PATCH'])
def update(request, pk):
    icu = Incubator.objects.get(id=pk)
    serializers = IncubatorSerializer(instance=icu, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
