from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from posts.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Post
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

class PostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


    if request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
