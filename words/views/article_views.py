from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from words.serializers import *
import json


@api_view(['POST'])
def article(request):
  if request.method == 'POST':
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


@api_view(['GET'])
def article_index(request):
  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True)
  return Response(serializer.data)


def article_show(request, pk):
  article = Article.objects.get(pk=pk)
  context = {'id': article.id,
             'title': article.title, }
  return render(request, 'articles/show.html', context)


def article_all(request):
  articles = Article.objects.all().order_by('title')
  context = {'articles': list(articles.values())}
  return render(request, 'articles/index.html', context)


def article_chart(request, pk):
  article = Article.objects.get(pk=pk)
  res = Article.objects.article_n_content(article)
  words = list(res['Content'].keys())[:10]
  count = list(res['Content'].values())[:10]
  count.append(0)
  return JsonResponse(data={
      'labels': words,
      'data': count
  })


def delete_article(request, pk):
  Article.objects.get(pk=pk).delete()
  return redirect('article_all')


def article_new(request):
  return render(request, 'articles/new.html')


def article_post(request):
  title = request.POST['title']
  content = request.POST['content']
  article = Article.objects.create_article(title, content)
  art_id = article['id']
  return redirect('article_show', pk=art_id)
  # return redirect('article_all)


# REQUEST METHODS
# request.method
# request.query_params['input_param']
# request.headers
