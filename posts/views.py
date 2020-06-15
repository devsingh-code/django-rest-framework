from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Author,Post
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import PostSerializer
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

class PostListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
