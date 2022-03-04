from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from author.models import Author
from notification.models import Notification


# Create your views here.
class NotificationsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, user_id):
        # gets a list of authors who are user_id's followers
        try:
            author = Author.objects.get(id=user_id)
            notifications = Notification.objects.filter(author=author)
            result = {
                "type": "inbox",
                "items": [n.content.toJson() for n in notifications]
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHORs_ID
        try:
            author = Author.objects.get(id=user_id)
            notifications = Notification.objects.filter(author=author)
            for n in notifications:
                notifications.delete()
            return response.Response("Deleted", status.HTTP_200_OK)
        except Exception as e:
            return response.Response(f"Error while trying to delete: {e}", status=status.HTTP_404_NOT_FOUND)
