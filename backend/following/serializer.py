from rest_framework import serializers

from author.serializer import AuthorSerializer
from author.models import Author

class FollowRequestModel:
    def __init__(self, follower: Author, author: Author) -> None:
        self.follower = follower
        self.author = author
    
    def getSummary(self):
        return self.follower.display_name + " wants to follow " + self.author.display_name

class FollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRequestModel
        fields = ()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["type"] = "Follow"
        representation["summary"] = instance.getSummary()
        representation["actor"] = AuthorSerializer(instance.follower, many=False).data
        representation["object"] = AuthorSerializer(instance.author, many=False).data
        return representation
