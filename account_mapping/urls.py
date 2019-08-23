from account_mapping.viewsets import AccountMappingViewSet, MandatorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mapping', AccountMappingViewSet, basename='map')
router.register(r'mandators', MandatorViewSet, basename='mandators')
urlpatterns = router.urls
