from django.contrib import admin
from django.urls import path, include
import user
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


@api_view(http_method_names=["GET"])
def healthcheck(request):
    return Response({"Status":"Up"}, status=200)

urlpatterns = [
    path('healthcheck/',healthcheck),
    path('api/v1/',include("user.urls"), name="users"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]