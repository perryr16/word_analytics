from django.db import models

# Create your models here.
class Word(models.Model):
  word = models.CharField(max_length=99, unique=True)
  length = models.IntegerField()

  def __str__(self):
    return self.word
