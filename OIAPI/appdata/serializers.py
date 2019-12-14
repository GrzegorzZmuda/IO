from rest_framework import serializers
from .models import Appdata

class AppdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appdata
        fields = '__all__'