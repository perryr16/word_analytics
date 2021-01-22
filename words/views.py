from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from words.models import Word, Article, ArticleWord

# Create your views here.
def home(request):
  tmpl_vars = {'from': PostForm()}
  return render(request, 'words/index.html', tmpl_vars)
# I DONT THINK THIS IS CORRECT 

@api_view(['GET'])
def word_index(request):
  if request.method == 'GET':
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def word_show(request, pk):
  try: 
    word = Word.objects.get(pk=pk)
  except Word.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WordSerializer(word)
    return Response(serializer.data)