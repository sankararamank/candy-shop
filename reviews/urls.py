from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register("", ReviewViewSet, "reviews")
urlpatterns = router.urls
