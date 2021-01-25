from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from words.models import Word, Article, ArticleWord
from words.serializers import WordSerializer

# Create your views here.
def home(request):
  tmpl_vars = {'from': PostForm()}
  return render(request, 'words/index.html', tmpl_vars)
# I DONT THINK THIS IS CORRECT 

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

    # REQUEST METHODS
    # request.method 
    # request.query_params['input_param']
    # request.headers

@api_view(['POST'])
def word_dump(request):
  words = Article.sort_words(request.body)
  return words


@api_view(['GET'])
def word_show(request, pk):
  try: 
    word = Word.objects.get(pk=pk)
  except Word.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WordSerializer(word)
    return Response(serializer.data)

