from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/', include('user.urls')),
    path('doctor/', include('doctor.urls')),
    path('schedule/', include('schedule.urls')),
    path('patient/', include('patient.urls')),
    path('surgery/', include('surgery.urls')),
    path('icu/', include('icu.urls')),
    path('incubator/', include('incubator.urls')),
    path('bloodbank/', include('bloodbank.urls')),
    path('service/', include('service.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

