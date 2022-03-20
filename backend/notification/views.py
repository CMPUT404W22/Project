from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from author.models import Author
from post.models import Post
from like.models import LikePost
from like.models import LikeComment
from like.views import save_like_post
from like.views import save_like_comment
from comment.models import Comment
from notification.models import Notification
from following.models import FollowRequest
from post.serializer import PostSerializer
from like.serializer import LikePostSerializer, LikeCommentSerializer
from comment.serializer import CommentSerializer
from following.serializer import FollowRequestSerializer

# Create your views here.
class NotificationsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    post_serializer = PostSerializer

    def get(self, request, user_id):
        author = Author.objects.get(id=user_id)
        notifications = Notification.objects.filter(author=author)
        notifications.order_by('-created')

        try:
            items = []

            n: Notification
            for n in notifications:
                items.append(n.content)

            result = {
                "type": "inbox",
                "items": [i.data for i in items]
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(f"Failed to get notifications: {e}", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, user_id):
        author = Author.objects.get(id=user_id)
        try:
            content = request.data['content']
            Notification.objects.create(author=author, content=content)
            return response.Response("Added notification", status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response(f"Failed to post to inbox: {e}", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        try:
            author = Author.objects.get(id=user_id)
            notifications = Notification.objects.filter(author=author)
            # delete all notifications
            for n in notifications:
                n.delete()
            return response.Response("Deleted", status.HTTP_200_OK)
        except Exception as e:
            return response.Response(f"Error while trying to delete: {e}", status=status.HTTP_400_BAD_REQUEST)
