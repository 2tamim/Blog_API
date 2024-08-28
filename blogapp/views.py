from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Post
from .serializers import BlogSerializer, PostSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, serializers.ValidationError):
            response.data['detail'] = 'خطا در اعتبارسنجی ورودی‌ها.'
        else:
            response.data['detail'] = 'خطای ناشناخته‌ای رخ داده است.'
        return response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, serializers.ValidationError):
            response.data['detail'] = 'خطا در اعتبارسنجی ورودی‌ها.'
        else:
            response.data['detail'] = 'خطای ناشناخته‌ای رخ داده است.'
        return response
