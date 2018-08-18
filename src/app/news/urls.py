from django.urls import include, path
from rest_framework import routers

from news import views

news_router = routers.DefaultRouter()
news_router.register('articles', views.ArticleViewSet)
news_router.register('comments', views.CommentViewSet)

app_name = 'news'
urlpatterns = [
    path('api/news/', include(news_router.urls)),
]
