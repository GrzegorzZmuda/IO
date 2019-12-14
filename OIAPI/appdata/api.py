from .models import Appdata
from rest_framework import viewsets, permissions
from .serializers import AppdataSerializer

class AppdataViewSet(viewsets.ModelViewSet):
    queryset = Appdata.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppdataSerializer
