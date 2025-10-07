
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet

app_name = "Assignment"

router = DefaultRouter()
router.register(r'assignment', AssignmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
]
