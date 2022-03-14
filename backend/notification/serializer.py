from rest_framework import serializers
from notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['type'] = "inbox"
        representation['author'] = f"http://127.0.0.1:8000/authors/{instance.author}"
        representation['url'] = f"http://127.0.0.1:8000/authors/{instance.id}"
        representation['host'] = "http://127.0.0.1:8000/"
        representation['displayName'] = instance.display_name
        representation['github'] = instance.github
        representation['profileImage'] = instance.image

        return representation
