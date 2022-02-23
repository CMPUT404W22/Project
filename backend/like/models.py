import uuid

from django.db import models

from author.models import Author
from post.models import Post


class Like(models.Model):
    like_id = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('author', 'post',)

    def __str__(self):
        return f"{self.author} liked ({self.post})"

