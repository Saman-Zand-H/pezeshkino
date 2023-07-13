from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from iranian_cities.models import Province, City


class ShahrSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ["name", "id"]
        
        
class OstanSerializer(ModelSerializer):
    cities = serializers.SerializerMethodField()
    
    class Meta:
        model = Province
        fields = ["name", "cities", "id"]
        
    def get_cities(self, obj):
        cities = obj.cities.all()
        return ShahrSerializer(cities, many=True).data
        