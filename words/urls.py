# words urls 
from django.urls import path 
from . import views

urlpatterns = [
  path('db/<int:pk>', views.word_show, name='word_show'),
  path('db', views.word_index, name='word_index'),
  path('db/article', views.article, name='article'),
  path('db/articles', views.article_index, name='article_index'),
  path('db/article/<int:pk>', views.article_get, name='article_get'),
  path('articles/<int:pk>', views.article_show, name='article_show'),
  path('articles', views.article_all, name='article_all'),
  path('article_chart/<int:pk>', views.article_chart, name='article_chart'),
  path('article/<int:pk>/delete', views.delete_article, name='delete_article'),
  path('article/new', views.article_new, name='article_new'),
  path('article/post', views.article_post, name='article_post'),
]
