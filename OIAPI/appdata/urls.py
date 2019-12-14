from rest_framework import routers
from .api import AppdataViewSet

router = routers.DefaultRouter()
router.register('api/appdata',AppdataViewSet,'appdata')

urlpatterns = router.urls