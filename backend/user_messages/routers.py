from rest_framework.routers import DefaultRouter

from .viewsets import UserMessageViewSet

router = DefaultRouter()
router.register("user_messages", UserMessageViewSet, basename="user_messages")
