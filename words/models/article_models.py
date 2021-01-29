from django.db import models
from .word_models import Word

class ArticleManager(models.Manager):
  def create_article(self, title, body):
    article = self.create(title=title)
    word_list = self.word_list(body)
    for word in word_list:
      word_obj = self.create_words(word, word_list)
      self.create_content(word_obj, word, word_list, article)
    article.save()
    res = self.article_n_content(article)
    return res

  def article_n_content(self, article):
    ord_content = sorted(list(article.content.values(
        'content', 'count')), key=lambda key: key['count'], reverse=True)
    # ord_dict = []
    ord_dict = {}
    for kv in ord_content:
      # x = {kv['content'] : kv['count']}
      # ord_dict.append(x)
      ord_dict[kv['content']] = kv['count']
    res = {'Title': article.title, 'Content': ord_dict, 'id': article.id}
    return res

  def create_words(self, word, word_list):
    try:
      word_obj = Word.objects.get(word=word)
    except:
      word_obj = Word(word=word, length=len(word))
      word_obj.save()
    return word_obj

  def create_content(self, word_obj, word, word_list, article):
    try:  # if it exists
      content_obj = ArticleWord.objects.get(word=word_obj, article=article)
      content_obj.count += 1
      content_obj.save()
    except:  # if it doesnt
      content_obj = ArticleWord(
          word=word_obj, article=article, count=1, content=word)
      content_obj.save()

  def word_list(self, string):
    body = str(string).lower()
    body = self.remove_punctuation(body)
    body = self.remove_small_words(body)
    word_list = body.split(' ')
    word_list = self.remove_special_characters(word_list)
    return word_list

  def remove_punctuation(self, body):
    punctuation = ['(', ')', '.', ',', ':', ';',
                   ',', '"', '[', ']', '/', ' - ']
    for element in punctuation:
      body = body.replace(element, '')
    return body

  def remove_small_words(self, body):
    small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' at ' ' be ', ' by ', ' for ', 'form-data', ' from ',
                   ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' on ', ' to ', ' that ', ' the ',  ' this ', ' with ', ' was ']
    for small in small_words:
      body = body.replace(small, ' ')
    return body

  def remove_special_characters(self, word_list):
    for word in word_list:  # 1234
      if '\\' in word:
        word_list.remove(word)
    while('' in word_list):
      word_list.remove('')
    return word_list
    # return word_list[1:]

  def serialize_article(self, article):
    res = {}
    res['title'] = article.title
    res['content'] = article.content


class Article(models.Model):
  url = models.TextField()
  title = models.TextField(unique=True)
  words = models.ManyToManyField(Word, through='ArticleWord')

  objects = ArticleManager()

  def __str__(self):
    return self.url


class ArticleWord(models.Model):
  word = models.ForeignKey(
      Word, related_name='content', on_delete=models.CASCADE)
  article = models.ForeignKey(
      Article, related_name='content', on_delete=models.CASCADE)
  count = models.IntegerField(default=0)
  content = models.TextField(default=None)
