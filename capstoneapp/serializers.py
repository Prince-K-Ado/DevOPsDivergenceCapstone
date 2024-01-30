from rest_framework import serializers
from . models import Capstoneapp

class CapstoneappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capstoneapp
        fields = '__all__'