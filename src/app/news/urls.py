from django.urls import include, path
from rest_framework import routers

from news import views

news_router = routers.DefaultRouter()
news_router.register('', views.ArticleViewSet)

app_name = 'articles'
urlpatterns = [
    path('api/articles/', include(news_router.urls)),
]
