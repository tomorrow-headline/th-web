from django.contrib import admin

from news import models

admin.site.register(models.Article)
admin.site.register(models.Comment)
