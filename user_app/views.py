from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
import requests
# Create your views here.


@api_view(['get'])
def get_single_user(request,pk):    
    user = User.objects.get(id = pk)
    serializer  = UserSerializer(user)
    return Response(serializer.data, status=200)


@api_view(['post'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password= request.data.get('password')
    user = get_user_model().objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('incorrect password')
    response = Response()
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint,data=request.data).json()
    response.data = {
        'access_token':tokens.get('access'),
        'refresh_token':tokens.get('refresh'),
        'email': user.email
    }
    return response

@api_view(["get","options"])
def get_current_user(request):
    user_profile = User.objects.get(email=request.user.email)
    serializer = UserSerializer(user_profile)
    return Response({'user':serializer.data})
    

@api_view(["get","options"])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)