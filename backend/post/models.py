import uuid

from django.db import models
from django.db.models import CharField, Model
from django_mysql.models import ListCharField
from django.utils.translation import gettext_lazy as _

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
    title = models.TextField(blank=False, null=False, default="title")
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    visibility = models.IntegerField(default=Visibility.PUBLIC, choices=Visibility.choices)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    unlisted = models.BooleanField(default=False)
    image = models.CharField(_('post image'), max_length=300, blank=True, null=True)
    categories = ListCharField(
        null=True,
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominal, plus commas
    )

    def get_author(self):
        return Author.objects.get(id=self.author.id)