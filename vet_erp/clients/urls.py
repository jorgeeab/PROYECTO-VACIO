from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, PetViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'pets', PetViewSet)

urlpatterns = router.urls
