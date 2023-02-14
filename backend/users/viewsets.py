from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


@extend_schema(tags=["Пользователи"])
class UserViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = UserSerializer
    queryset = User.objects.all()
