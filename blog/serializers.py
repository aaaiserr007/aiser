from rest_framework import serializers
from .models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Показывать имя автора, но не редактировать

    class Meta:
        model = Comment
        fields = ['id', 'blog_post', 'author', 'content', 'created_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Комментарий не может быть пустым.")
        return value

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Показывать имя автора, но не редактировать
    comments = CommentSerializer(many=True, read_only=True)  # Вложенные комментарии

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'comments']