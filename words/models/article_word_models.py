from django.db import models
from .word_models import Word
from .article_models import Article 


class ArticleWord(models.Model):
  word = models.ForeignKey(
      Word, related_name='content', on_delete=models.CASCADE)
  article = models.ForeignKey(
      Article, related_name='content', on_delete=models.CASCADE)
  count = models.IntegerField(default=0)
  content = models.TextField(default=None)
