from django.db import models

# Create your models here.
class Word(models.Model):
  word = models.CharField(max_length=99, unique=True)
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
    # body = self.repalce_words(body)
    punctuation = ['(', ')', '.', ',', ':', ',', '"', '[', ']', '/']
    for element in punctuation:
      body = body.replace(element, '')

    small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' be ', ' by ', ' for ', ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' to ', ' the ']
    for small in small_words:
      body = body.replace(small, ' ')

    word_list = body.split(' ')
    word_dict = {}

    for word in word_list: 
      if "\\" not in word:
        word_dict[word] = word_dict.get(word, 0) + 1
    word_sort = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))
    return word_sort

  def create_words(body):
    body = str(body).lower()
    punctuation = ['(', ')', '.', ',', ':', ',', '"', '[', ']', '/']
    for element in punctuation:
      body = body.replace(element, '')

    small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' be ', ' by ', ' for ', ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' to ', ' the ']
    for small in small_words:
      body = body.replace(small, ' ')

    word_list = body.split(' ')

    for word in word_list:
      if Word.objects.filter(word=word):
        a_w = ArticleWord.objects.filter(word=word)
      else: 
        a_w = ArticleWord(word=word, count=1)
        a_w.count += 1
        a_w.save()
      
        
      word = Word(word=word, length=len(word))
      
      article_word = None


  # def replace_words(self, **kwargs):
  #   replacements = ['(', ')', '.', ',', ':', '[', ']', '/', 'a', 'i', 'to', 'an', 'the', 'in']
  #   for element in replacements:
  #     body.replace(element, '')
  #   return string

class ArticleWord(models.Model):
  word = models.ForeignKey(Word, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  count = models.IntegerField(blank=True, null=True)
