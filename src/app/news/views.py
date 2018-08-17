from rest_framework import viewsets

from news import models, serializers


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
