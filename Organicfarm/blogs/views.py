from .serializers import ArticleCommentSerializer
from .models import ArticleComment
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GetArticleView(APIView):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                category = article.category.all().values_list('name', flat=True)
                comments = ArticleComment.objects.filter(article=article)
                serializer = ArticlesSerializer(article)
                serializer.data['category'] = list(category)
                serializer.data['comments'] = [{'comment': comment.comment_field} for comment in comments]
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': "No article found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            articles = Article.objects.all()
            articles_data = ArticlesSerializer(articles, many=True).data
            return Response(data=articles_data, status=status.HTTP_200_OK)


class ArticleByCategory(APIView):
    def get(self, request, category):
        try:
            articles_in_category = Article.objects.filter(
                categories__name=category)
            if articles_in_category.exists():
                serializer = ArticlesSerializer(articles_in_category, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No articles found in this category'}, status=status.HTTP_404_NOT_FOUND)
        except Articlescategory.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class CreateComment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, article_id):
        try:
            article = ArticleComment.objects.get(id=article_id)
        except ArticleComment.DoesNotExist:
            return Response({'error': "No article found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetComments(APIView):
    def get(self, request, article_id):
        try:
            article = ArticleComment.objects.get(id=article_id)
            comments = ArticleComment.objects.filter(article=article)
            serializer = ArticleCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ArticleComment.DoesNotExist:
            return Response({'error': "No article found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateComment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, comment_id):
        try:
            comment = ArticleComment.objects.get(id=comment_id)
            if comment.user.id != request.user.id:
                return Response({'error': "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            serializer = ArticleCommentSerializer(
                comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': "No comment found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteComment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, comment_id):
        try:
            comment = ArticleComment.objects.get(id=comment_id)
            if comment.user.id == request.user.id:
                comment.delete()
                return Response({'msg': "comment Deleted"}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response({'error': "No comment found"}, status=status.HTTP_404_NOT_FOUND)
