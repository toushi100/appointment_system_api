from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import BloodBank
from .filters import *
from .serializers import *

@api_view(['GET'])
def index(request):
    filters = request.data.get('filters', {})
    donations = BloodBank.objects.all()
    donations = BloodBankFilter(request.GET, queryset=donations).qs
    serializers = ShowBloodBankSerializer(donations, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializers = BloodBankSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)