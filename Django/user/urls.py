from django.urls import path
from user import views


# Type 1: Django function based view
# urlpatterns = [
#     path('users/', views.user_list),
#     path('users/<int:pk>/', views.user_detail),
# ]



# Type 2 : Django class based view
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

# Type 3 : DRF function based view
# urlpatterns = [
#     path('users/', views.user_list),
#     path('users/<int:pk>/', views.user_detail),
# ]

# Type 4 : DRF class based view
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]


# Type 5 : DRF mixin based view
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]


# Type 6 : DRF generic based view
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]



# Type 7 : DRF viewsets based view
from .views import UserViewSet
from rest_framework import renderers


from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


