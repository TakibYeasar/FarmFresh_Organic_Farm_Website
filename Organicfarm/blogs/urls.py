from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', GetArticleView.as_view(), name='article-list'),
    path('articles/<int:id>/', GetArticleView.as_view(), name='article-detail'),
    path('articles/categories/<str:category>/',
         ArticleByCategory.as_view(), name='articles-by-category'),
    path('articles/<int:article_id>/comments/create/',
         CreateComment.as_view(), name='comment-create'),
    path('articles/<int:article_id>/comments/',
         GetComments.as_view(), name='comment-list'),
    path('comments/<int:comment_id>/update/',
         UpdateComment.as_view(), name='comment-update'),
    path('comments/<int:comment_id>/delete/',
         DeleteComment.as_view(), name='comment-delete'),
]
