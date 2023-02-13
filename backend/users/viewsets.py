from drf_spectacular.utils import extend_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.serializers import UserSerializer


@extend_schema(tags=["Пользователи"])
class UserViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
