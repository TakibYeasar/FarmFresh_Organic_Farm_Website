from rest_framework import serializers
from .models import *


class ContactinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactinfo
        fields = "__all__"

    
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url
    
    

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class AboutitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutitem
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
        depth = 1
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = AboutitemSerializer(instance.item, context={'request':request}).data
        return response
    


class ServiceitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serviceitem
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        depth = 1
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = ServiceitemSerializer(instance.item, context={'request':request}).data
        return response
    


class WhychooseitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychooseitem
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class WhychooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose
        fields = "__all__"
        depth = 1
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = WhychooseitemSerializer(instance.item, context={'request':request}).data
        return response
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        depth = 1

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


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
        response['item'] = ProductitemSerializer(
            instance.item, context={'request': request}).data
        return response


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"
        depth = 1
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = WhychooseitemSerializer(instance.item, context={'request':request}).data
        return response
    

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
