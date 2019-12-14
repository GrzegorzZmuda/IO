from rest_framework import serializers
from .models import Logdata

class LogdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logdata
        fields = '__all__'