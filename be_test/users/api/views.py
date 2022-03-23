from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from .serializers import UserSerializer, KeyboardSerializer, KeycapSerializer
from be_test.users.models import Keyboard, Keycap

User = get_user_model()

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class KeyboardViewSet(ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Keyboard.objects.all().order_by('-created_at')
    serializer_class = KeyboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class KeycapViewSet(ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Keycap.objects.all().order_by('-created_at')
    serializer_class = KeycapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
