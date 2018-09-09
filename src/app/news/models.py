from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify


class Profile(models.Model):
    nickname = models.CharField(max_length=20)
    bio = models.TextField(max_length=500, blank=True)
    ico = models.ImageField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


@receiver(signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            nickname=slugify(instance.username)
        )


@receiver(signals.post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    ref = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.content
