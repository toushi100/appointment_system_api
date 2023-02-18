from rest_framework import status
from .models import IntensiveCareUnit
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create(request):
    serializers = IntensiveCareUnitSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)