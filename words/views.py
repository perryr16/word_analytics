from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from words.models import Word, Article, ArticleWord, ArticleManager
from words.serializers import WordSerializer, ArticleSerializer, ArticleWordSerializer
import json 


@api_view(['GET', 'POST'])
def word_index(request):
  if request.method == 'GET':
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
  if request.method == 'POST':
    param = request.query_params['word']
    new_word = Word(word=param, length=len(param))
    new_word.save()
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def article(request):
  if request.method=='POST':
    body = request.data['body']
    title = request.data['title']
    res = Article.objects.create_article(title, body)
  return Response(res)

@api_view(['GET'])
def article_get(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    return HttpResponse(status=404)
  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    # return Response(article.objects.values())
    return Response(Article.objects.article_n_content(article))

  # title = request.query_params['title']
  # article = Article.objects.create_article(title, request.body)
  # # article = Article(title=title)
  # # article.save
  # # word = Word(word='tuna', length=4)
  # # word.save()
  # import pdb; pdb.set_trace()
  # return Response(json.dumps({"word":"word"}))
  # return HttpResponse(json.dumps({"words":"word"}))
  # return HttpResponse(json.dumps(words))


@api_view(['GET'])
def word_show(request, pk):
  try: 
    word = Word.objects.get(pk=pk)
  except Word.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WordSerializer(word)
    return Response(serializer.data)

@api_view(['GET'])
def article_index(request):
  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True)
  return Response(serializer.data)


# REQUEST METHODS
# request.method
# request.query_params['input_param']
# request.headers

def article_show(request, pk):
  article = Article.objects.get(pk=pk)
  res = Article.objects.article_n_content(article)
  context = res
  return render(request, 'articles/show.html', context)
