from django.db import models

# Create your models here.
class Word(models.Model):
  word = models.CharField(max_length=99, unique=True)
  length = models.IntegerField()

  def __str__(self):
    return self.word

class ArticleManager(models.Manager):
  def create_article(self, title, body):
    article = self.create(title=title)
    word_list = self.word_list(body)
    for word in word_list:
      try: 
        new_word = Word(word=word, length=len(word))
        new_word.save()
      except: 
        new_word = Word.objects.get(word='see')
        pass

      aw = ArticleWord.objects.get_or_create(word_id=new_word.id, article_id=article.id)[0]
      if aw.count is 0:
        aw.count = 1
        aw.save()
      else: 
        aw.count += 1 
        aw.save()

    article.save()
    import pdb; pdb.set_trace()
    return article

  def word_list(self, string):
    body = str(string).lower()
    # body = self.repalce_words(body)
    punctuation = ['(', ')', '.', ',', ':', ',', '"', '[', ']', '/']
    for element in punctuation:
      body = body.replace(element, '')

    small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' be ', ' by ', ' for ', ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' to ', ' the ']
    for small in small_words:
      body = body.replace(small, ' ')

    word_list = body.split(' ')

    for word in word_list:
      if '\\' in word:
        word_list.remove(word)
    return word_list


class Article(models.Model):
  url = models.TextField()
  title = models.TextField(unique=True)
  words = models.ManyToManyField(Word, through='ArticleWord')

  objects = ArticleManager()
  def __str__(self):
    return self.url
  

class ArticleWord(models.Model):
  word = models.ForeignKey(Word, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  count = models.IntegerField(default=0)



  # def create_words(body):
  #   body = str(body).lower()
  #   punctuation = ['(', ')', '.', ',', ':', ',', '"', '[', ']', '/']
  #   for element in punctuation:
  #     body = body.replace(element, '')

  #   small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' be ', ' by ', ' for ', ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' to ', ' the ']
  #   for small in small_words:
  #     body = body.replace(small, ' ')

  #   word_list = body.split(' ')
  #   import pdb; pdb.set_trace()
  #   for word in word_list:
  #     if Word.objects.filter(word=word):
  #       a_w = ArticleWord.objects.filter(word=word)
  #     else: 
  #       a_w = ArticleWord(word=word, count=1)
  #       a_w.count += 1
  #       a_w.save()
      
        
  #     word = Word(word=word, length=len(word))
      
  #     article_word = None

    # def sort_words(body):
    #   body = str(body).lower()
    # # body = self.repalce_words(body)
    # punctuation = ['(', ')', '.', ',', ':', ',', '"', '[', ']', '/']
    # for element in punctuation:
    #   body = body.replace(element, '')

    # small_words = [' a ', ' an ', ' and ', ' are ', ' as ', ' be ', ' by ', ' for ', ' i ', ' in ', ' is ', ' it ', ' of ', ' or ', ' to ', ' the ']
    # for small in small_words:
    #   body = body.replace(small, ' ')

    # word_list = body.split(' ')
    # word_dict = {}

    # for word in word_list: 
    #   if "\\" not in word:
    #     word_dict[word] = word_dict.get(word, 0) + 1
    # word_sort = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))
    # return word_sort


      # a_w = ArticleWord.objects.filter(word=new_word).values('count')
      # if word == 'see':
      #   import pdb; pdb.set_trace()

      # ArticleWord.objects.values() = all values
      # (Pdb) aw = ArticleWord.objects.get(pk=2434)
      # (Pdb) aw.count
      # 1
      # (Pdb) aw.count += 1
      # (Pdb) aw.count
      # 2
      # ArticleWord.objects.values()
      #  breed = Word.objects.filter(word='breed').values('id')
      # (Pdb) breed[0]
      # {'id': 31537, 'word': 'breed', 'length': 5}

          # aw = ArticleWord.objects.filter(word_id=new_word.id).values()[0]["count"]

                  # count = a_w.count
        # count = a_w.count + 1
        # article.words.add(new_word, through_defaults={'count':'1'})