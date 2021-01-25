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
  
  def sort_words(body):
    body = str(body).lower()
    body =  body.replace('(', '').replace(')', '')
    word_list = body.split(' ')
    word_dict = {}
    for word in word_list: 
      if "\\" not in word:
        word_dict[word] = word_dict.get(word, 0) + 1
    word_sort = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))
    return word_sort
class ArticleWord(models.Model):
  word = models.ForeignKey(Word, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  count = models.IntegerField(blank=True, null=True)
