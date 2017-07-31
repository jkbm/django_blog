from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    edited_date = models.DateTimeField(
            blank=True, null=True)
    tags = models.CharField(
            max_length=400, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
        post = models.ForeignKey(Post)
        name = models.CharField(max_length=50)
        comment = models.TextField()
        published_date = models.DateTimeField(
                blank=True, null=True)
        edited_date = models.DateTimeField(
                blank=True, null=True)

        def __str__(self):
                return self.comment
