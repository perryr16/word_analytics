# words urls 
from django.urls import path 
from . import views

urlpatterns = [
  path('<int:pk>', views.word_show, name='word_show'),
  path('', views.word_index, name='word_index'),
  path('article', views.article, name='article'),
  path('articles', views.article_index, name='article_index'),
  path('article/<int:pk>', views.article_get, name='article_get'),
  path('artsy/<int:pk>', views.article_show, name='article_show'),
  path('artsy', views.article_all, name='article_all'),
  path('article_chart/<int:pk>', views.article_chart, name='article_chart'),
  path('delete_article/<int:pk>', views.delete_article, name='delete_article'),
  path('article/new', views.article_new, name='article_new'),
]
