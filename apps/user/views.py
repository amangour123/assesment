from rest_framework import viewsets
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrManager
from rest_framework.decorators import action
from rest_framework.response import Response

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrManager])
    def reactivate(self, request, pk=None):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
            return Response({'status': 'User reactivated'})
        return Response({'status': 'User already active'}, status=400)
