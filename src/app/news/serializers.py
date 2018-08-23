from rest_framework import serializers
from django.contrib.auth.models import User

from news import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('title', 'author', 'excerpt', 'content', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('author', 'content', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('url', 'nickname', 'bio', 'ico', )
