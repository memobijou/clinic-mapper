from account_mapping.viewsets import AccountMappingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mapping', AccountMappingViewSet, basename='map')
urlpatterns = router.urls
