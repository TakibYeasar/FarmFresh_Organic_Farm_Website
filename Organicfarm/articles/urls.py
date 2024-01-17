from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.GetArticleCategoriesView.as_view(),
         name='get_categories'),
    path('articles/', views.GetArticleView.as_view(), name='get_articles'),
    path('articles/<int:id>/', views.GetArticleView.as_view(),
         name='get_article_by_id'),
    path('articles/category/<int:category_id>/',
         views.ArticleByCategory.as_view(), name='articles_by_category'),
    path('articles/<int:article_id>/comments/',
         views.CreateComment.as_view(), name='create_comment'),
    path('articles/<int:article_id>/comments/',
         views.GetComments.as_view(), name='get_comments'),
    path('articles/<int:article_id>/comments/<int:comment_id>/',
         views.UpdateComment.as_view(), name='update_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/',
         views.DeleteComment.as_view(), name='delete_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/replies/',
         views.CreateReplyComment.as_view(), name='create_reply_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/replies/',
         views.GetReplyComments.as_view(), name='get_reply_comments'),
    path('articles/<int:article_id>/comments/<int:comment_id>/replies/<int:reply_comment_id>/',
         views.UpdateReplyComment.as_view(), name='update_reply_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/replies/<int:reply_comment_id>/',
         views.DeleteReplyComment.as_view(), name='delete_reply_comment'),
]
