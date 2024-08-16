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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


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

    def get_main_image(self, obj):
        return self.get_image_url(obj.main_image)
    
    def get_images(self, obj):
        return [self.get_image_url(image) for image in obj.images.all()]
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


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
