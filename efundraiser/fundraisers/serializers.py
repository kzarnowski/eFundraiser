from rest_framework import serializers

from .models import Fundraiser

class FundraiserSerializer(serializers.Serializer):
    class Meta:
        model = Fundraiser
        fields = '__all__'
