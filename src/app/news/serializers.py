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


class SpecificPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(SpecificPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(author=request.user)


class ProfileSerializer(serializers.ModelSerializer):
    comments = SpecificPrimaryKeyRelatedField(
        many=True,
        queryset=models.Comment.objects.all()
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
