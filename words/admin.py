from django.contrib import admin
from .models import Word, Article, ArticleWord

# Register your models here.

admin.site.register(Word)
admin.site.register(Article)
admin.site.register(ArticleWord)
