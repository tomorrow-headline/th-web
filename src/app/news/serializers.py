from django.contrib.auth.models import User
from rest_framework import serializers

from news import models


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Article
        fields = ('title', 'author', 'excerpt', 'content', 'comments', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('author', 'content', 'ref', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('url', 'nickname', 'bio', 'ico', )
