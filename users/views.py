from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import UserError
from .serializers import UserErrorSerializer


class UserErrorViewSet(viewsets.ModelViewSet):
    serializer_class = UserErrorSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = UserError.objects.all()
        return queryset
