from django.urls import path
from .views import *
urlpatterns =[
    path('create/', create),
    path('show/<int:pk>/', show),
    path('update/', update),
    path('index/', index),
]