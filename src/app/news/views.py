from rest_framework import viewsets
from news import models

from news import serializers


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    class Meta:
        queryset = models.Article.objects.all()
        serializer_class = serializers.ArticleSerializer
