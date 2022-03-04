from rest_framework import serializers

from author.serializer import AuthorSerializer
from following.models import Following


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation
