from rest_framework import serializers
from notification.models import Notification
from author.serializer import AuthorSerializer

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['type'] = "post"
        representation['title'] = instance.title
        representation['id'] = f'http://127.0.0.1:8000/authors/{instance.author.id}/posts/{instance.post.id}'
        representation['source'] = instance.source
        representation['source'] = instance.origin
        representation['description'] = instance.description
        representation['contentType'] = instance.contentType
        representation['content'] = instance.content
        representation['author'] = AuthorSerializer(instance.get_author(), many=False).data
        representation['content'] = instance.categories
        representation['comments'] = f'http://127.0.0.1:5454/authors/{instance.author.id}/posts/{instance.post.id}/comments'
        representation['published'] = instance.published
        representation['visibility'] = instance.visibility
        representation['unlisted'] = instance.unlisted
        
        return representation
