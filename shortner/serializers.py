from rest_framework import serializers
from .models import ShortUrl

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'
        