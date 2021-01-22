from django.db import models

# Create your models here.
class Word(models.Model):
  word = models.CharField(max_length=99)
  length = models.IntegerField()

  def __str__(self):
    return self.word

class Article(models.Model):
  url = models.TextField()
  title = models.TextField()
  words = models.ManyToManyField(Word, through='ArticleWord')

  def __str__(self):
    return self.url

class ArticleWord(models.Model):
  word = models.ForeignKey(Word, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  count = models.IntegerField(blank=True, null=True)
