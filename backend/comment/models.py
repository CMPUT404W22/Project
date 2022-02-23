import uuid

from django.db import models

from author.models import Author
from post.models import Post


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} | {self.content}"



