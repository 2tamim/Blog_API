from rest_framework import serializers
from .models import Blog, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_image(self, value):
        if value and not value.name.endswith('.jpg'):
            raise serializers.ValidationError("فقط فرمت JPG قابل قبول است.")
        return value

class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
