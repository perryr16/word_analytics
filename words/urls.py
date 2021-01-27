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
]
