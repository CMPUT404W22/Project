import uuid

from django.db import models

from author.models import Author


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE)
    notification_type = models.TextField(blank=False, null=False)
    notification_id = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
