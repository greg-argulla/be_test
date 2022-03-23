from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from be_test.users.api.views import UserViewSet, KeyboardViewSet, KeycapViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("keyboard", KeyboardViewSet)
router.register("keycap", KeycapViewSet)

app_name = "api"
urlpatterns = router.urls
