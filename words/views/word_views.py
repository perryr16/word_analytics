import json
from words.serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from ..models import *
from words.serializers import *


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


@api_view(['GET'])
def word_show(request, pk):
  try: 
    word = Word.objects.get(pk=pk)
  except Word.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WordSerializer(word)
    return Response(serializer.data)
