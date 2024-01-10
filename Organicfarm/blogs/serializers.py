from rest_framework import serializers
from .models import *


class ArticlescategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlescategory
        fields = "__all__"
        # depth = 1
        
        
class ArticlestagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlestag
        fields = "__all__"
        # depth = 1
        

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # depth = 1

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url
    
    
    
class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = "__all__"
        # depth = 1
        
        