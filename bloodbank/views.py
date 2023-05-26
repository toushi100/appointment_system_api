from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import BloodBank, BloodbankRequest
from rest_framework.reverse import reverse
from .filters import *
from .serializers import *
import requests
@api_view(['GET'])
def   total_amount(request, blood_type):
    amount = BloodBank.objects.total_amount(blood_type)
    response={
        "blood_type": blood_type,
        "amount_in_bags": amount['amount__sum']
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializers = BloodBankSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def create_bloodbank_request(request):

    amount = reverse(viewname= 'total_amount', request=request, args=[request.data['blood_type']])
    amount = requests.get(amount).json()
    if request.data['amount'] > amount.get('amount_in_bags'):
        return Response({'error': 'amount is greater than available amount'}, status=status.HTTP_400_BAD_REQUEST)
    serializers = BloodBankRequestSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)