from django.db import models
from django.conf import settings          # ← добавить этот импорт
from wagtail.models import Page
from django.utils import timezone


class Comment(models.Model):
    article = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # ← заменили
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Like', related_name='liked_comments')  # если используешь через, или просто добавим метод

    class Meta:
        ordering = ['created_at']

    def is_liked_by(self, user):
        return self.comment_likes.filter(user=user).exists()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')
