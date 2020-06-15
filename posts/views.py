from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,

)
from .models import Author,Post
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import PostSerializer,PostCreateSerializer, AuthorSerializer
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def post_detail(request, pk):
    return render(request,'post_detail.html')

class AuthorDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class PostListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostCreateView(CreateAPIView):
    permission_classes =(AllowAny,)
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    permission_classes =(AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostUpdateView(UpdateAPIView):
    permission_classes =(AllowAny,)
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
