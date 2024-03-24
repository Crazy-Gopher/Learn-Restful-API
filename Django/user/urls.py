from rest_framework import routers
from user import views
from user import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)