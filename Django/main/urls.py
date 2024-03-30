from django.contrib import admin
from django.urls import path, include
from user.urls import router

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET"])
def healthcheck(request):
    return Response({"Status":"Up"}, status=200)

urlpatterns = [
    path('healthcheck/',healthcheck),
    # path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls), name="users")
]
