from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create, name='create'),
    path('reserved_icu_beds/', reserved_icu_beds, name='reserved_icu_beds'),
    path('update/<int:pk>/', update, name='update'),
]