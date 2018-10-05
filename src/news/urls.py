from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from news import views

news_router = routers.DefaultRouter()
news_router.register('articles', views.ArticleViewSet)
news_router.register('comments', views.CommentViewSet)
news_router.register('users', views.ProfileViewSet)
news_router.register('tags', views.TagViewSet)

app_name = 'news'
urlpatterns = [
    path('api/news/', include(news_router.urls)),
    path('news/', TemplateView.as_view(template_name='index.html')),
]
