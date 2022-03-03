import uuid

from django.db import models

from author.models import Author
from django.db.models import CharField, Model
from django_mysql.models import ListCharField



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
    title = models.TextField(blank=False, null=False, default="title")
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    visibility = models.IntegerField(default=Visibility.PUBLIC, choices=Visibility.choices)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now_add=True, editable=False)
    count = models.IntegerField(default=0)
    unlisted = models.BooleanField(default=False)
    categories = ListCharField(
        null=True,
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
    )

    def get_author(self):
        # print(self.author)
        return Author.objects.get(id=self.author.id)

    def toJson(self):
        return {
            "type": "post",
            "title": self.title,
            "id": f'http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.id}',
            "description": self.description,
            "contentType":self.type,
            "content": self.content,
            "author": self.get_author().toJson(),
            "categories": self.categories,
            "count": self.count,
            "comments": f'http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.id}/comments',
            "published": self.updated,
            "visibility": self.visibility,
            "unlisted": self.unlisted
        }
