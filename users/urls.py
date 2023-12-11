from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import re_path as url

from .views import UserErrorViewSet

APPEND_SLASH = False

router = SimpleRouter(trailing_slash=False)
router.register(r"users", UserErrorViewSet, "users")

app_name = "users"
urlpatterns = [url(r"^", include(router.urls))]