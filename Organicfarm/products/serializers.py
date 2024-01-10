from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    
class ProductitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productitem
        fields = "__all__"
        depth = 1
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url
    

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['product'] = ProductitemSerializer(
            instance.product, context={'request': request}).data
        return response
    

class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 1

