from django.db import models

from author.models import Author


class Following(models.Model):
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    objects = models.Manager()

    class Meta:
        unique_together = ('author', 'following',)

    def save(self, *args, **kwargs):
        if self.author != self.following:
            return super().save(*args, **kwargs)
        else:
            raise Exception("Authors cannot follow themselves")

    def get_author(self):
        return Author.objects.get(id=self.author.id)

    def __str__(self):
        return f"{self.author} is following ({self.following})"


