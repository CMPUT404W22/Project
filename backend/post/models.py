import uuid

from django.db import models

from author.models import Author


class Visibility(models.IntegerChoices):
    PUBLIC = 0, 'Public'
    FRIENDS = 1, 'Friends'
    PRIVATE = 2, 'Private'


class PostType(models.IntegerChoices):
    PLAINTEXT = 0, 'Plain Text'
    COMMONMARK = 1, 'Common Mark'
    LINK = 2, 'Image Link'
    IMAGE = 3, 'Image File'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE)
    type = models.IntegerField(default=PostType.PLAINTEXT, choices=PostType.choices)
    content = models.TextField(blank=True, null=True)
    visibility = models.IntegerField(default=Visibility.PUBLIC, choices=Visibility.choices)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} | {self.content}"
