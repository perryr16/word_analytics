# words urls 
from django.urls import path 
from . import views

urlpatterns = [
  path('<int:pk>', views.word_show, name='word_show'),
  path('', views.word_index, name='word_index')
]