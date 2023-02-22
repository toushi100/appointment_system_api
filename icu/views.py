from rest_framework import status
from .models import IntensiveCareUnit
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .filters import IntensiveCareUnitFilter


@api_view(['POST'])
def create(request):
    serializers = IntensiveCareUnitSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def reserved_icu_beds(request):
    
    filters = request.data.get('filters', {})
    icu = IntensiveCareUnit.objects.filter(start_time__lte=timezone.now(), end_time= None)
    icu = IntensiveCareUnitFilter(filters, queryset=icu).qs
    serializers = showIntensiveCareUnitSerializer(icu, many=True)
    return Response(serializers.data)

@api_view(['PUT', 'PATCH'])
def update(request, pk):
    icu = IntensiveCareUnit.objects.get(id=pk)
    serializers = IntensiveCareUnitSerializer(instance=icu, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    