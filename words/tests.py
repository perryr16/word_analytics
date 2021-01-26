from django.test import TestCase
from .models import Word, Article, ArticleWord, ArticleManager

# Create your tests here.

class WordTestCase(TestCase):
  def setUp(self):
    self.pig = Article.objects.create(url='www.example.com', title='Pigs')
    self.word1 = Word.objects.create(word='pig', length=3)
    self.word2 = Word.objects.create(word='oink', length=4)
    self.word3 = Word.objects.create(word='cow', length=3)

    ArticleWord.objects.create(word=self.word1, article=self.pig, count=10)
    ArticleWord.objects.create(word=self.word2, article=self.pig, count=3)

  def test_auto_pass(self):
    self.assertEqual(1, 1)

  def test_words_in_article(self):
    import pdb; pdb.set_trace()
    self.assertEqual(self.word1.article.all(), self.pig)
  
  def test_article_has_words(self):
    words = list(self.pig.words.all())
    self.assertEqual(words, [self.word1, self.word2])
  
    import pdb; pdb.set_trace()