from rest_framework.routers import DefaultRouter
from .views import AIUserScaleViewSet

router = DefaultRouter()
router.register(r'aiuserscale', AIUserScaleViewSet, basename='aiuserscale')

urlpatterns = router.urls
