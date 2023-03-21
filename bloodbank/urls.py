from django.urls import path
from .views import *

urlpatterns = [
    path('total_amount/<str:blood_type>/', total_amount, name='total_amount'),
    path('create/', create, name='create'),
    path('create_bloodbank_request/', create_bloodbank_request, name='create_bloodbank_request')
    
]