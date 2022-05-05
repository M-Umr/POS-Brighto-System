from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from backend_app.views import POSViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"pos", POSViewSet)

app_name = "api"
urlpatterns = router.urls