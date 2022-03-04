from rest_framework import serializers

from author.serializer import AuthorSerializer
from like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['@context'] = "https://www.w3.org/ns/activitystreams"
        representation['summary'] = instance.summary
        representation['type'] = "author"
        representation['author'] = AuthorSerializer(instance.get_author(), many=False).data
        representation['object'] = f"http://127.0.0.1:5454/authors/{instance.author.id}/posts/{instance.post.id}"

        return representation
