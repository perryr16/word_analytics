from rest_framework import serializers
from words.models import *

class WordSerializer(serializers.ModelSerializer):
  class Meta:
    model = Word 
    fields = ('id', 'word', 'length')

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article 
    depth = 1
    fields = ('id', 'title', 'url')
class ArticleWordSerializer(serializers.ModelSerializer):
  class Meta:
    model = ArticleWord 
    fields = ('id', 'word', 'article', 'content', 'count')

