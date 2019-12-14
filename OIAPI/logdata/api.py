from .models import Logdata
from rest_framework import viewsets, permissions
from .serializers import LogdataSerializer

class LogdataViewSet(viewsets.ModelViewSet):
    queryset = Logdata.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LogdataSerializer
