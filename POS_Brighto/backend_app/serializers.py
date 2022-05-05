from rest_framework import serializers
from .models import POS_Table


class POSSerializer(serializers.ModelSerializer):
    class Meta:
        model = POS_Table
        fields = '__all__'