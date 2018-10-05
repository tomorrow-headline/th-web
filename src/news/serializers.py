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

    def create(self, validated_data):
        instance = super(UserSerializer, self).create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=True
    )
    user = UserSerializer()

    class Meta:
        model = models.Profile
        fields = ('user', 'nickname', 'bio', 'ico', 'comments', )

    def create(self, validated_data):
        user = UserSerializer.create(
            UserSerializer(),
            validated_data=validated_data['user']
        )
        validated_data['user'] = user

        return super(ProfileSerializer, self).create(validated_data)


class TagSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Tag
        fields = ('name', 'articles', )
