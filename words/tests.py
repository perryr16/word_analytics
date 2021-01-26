from django.test import TestCase
from .models import Word, Article, ArticleWord, ArticleManager

# Create your tests here.

class WordTestCase(TestCase):
  def setUp(self):
    self.article1 = Article.objects.create(url='www.example.com', title='article title')
    self.word1 = Word.objects.create(word='word1', length=5)
    self.word2 = Word.objects.create(word='word22', length=6)
    self.word3 = Word.objects.create(word='word333', length=7)

    self.aw1 = ArticleWord.objects.create(word=self.word1, article=self.article1, count=10)
    self.aw2 = ArticleWord.objects.create(word=self.word2, article=self.article1, count=3)

  def test_auto_pass(self):
    self.assertEqual(1, 1)

  def test_word_has_article(self):
    article = list(self.word1.article_set.all())[0]
    self.assertEqual(article, self.article1)
  
  def test_article_has_words(self):
    words = list(self.article1.words.all())
    self.assertEqual(words, [self.word1, self.word2])

  def test_article_has_content(self):
    content = list(self.article1.content.all())
    self.assertEqual(content, [self.aw1, self.aw2])

  def test_word_has_content(self):
    content = list(self.word1.content.all())[0]
    self.assertEqual(content, self.aw1)


  