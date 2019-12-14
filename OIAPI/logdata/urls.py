from rest_framework import routers
from .api import LogdataViewSet

router = routers.DefaultRouter()
router.register('api/logdata',LogdataViewSet,'logdata')

urlpatterns = router.urls