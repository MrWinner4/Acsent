#Converts HTTP Request data to Python data types and vice versa, basically just making the requests something django can understand
from .models import Product, UserPreference, UserProfile
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'features', 'photo')