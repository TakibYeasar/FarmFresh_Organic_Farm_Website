from rest_framework import serializers
from .models import *



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")


class AboutitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutitem
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
    
    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = AboutitemSerializer(instance.item, context={'request':request}).data
        return response



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"



class WhychooseitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychooseitem
        fields = "__all__"


class WhychooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose
        fields = "__all__"
    
    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        response['item'] = AboutitemSerializer(instance.item, context={'request':request}).data
        return response



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class ArticlescategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlescategory
        fields = "__all__"
    
    
class ArticlestagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlestag
        fields = "__all__"
    
    

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")




class ArticleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleReview
        fields = "__all__"



class ReplayArticleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplayArticleReview
        fields = "__all__"




class ContactSerialier(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
