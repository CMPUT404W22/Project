from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from author.models import Author
from post.models import Post
from like.models import LikePost
from like.models import LikeComment
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

        try:
            items = list()

            n: Notification
            for n in notifications:
                result = None
                if n.notification_type == "post":
                    post = Post.objects.get(id=n.notification_id)
                    result = PostSerializer(post, many=False)
                elif n.notification_type == "follow_request":
                    followRequest = FollowRequest.objects.get(id=n.notification_id)
                    result = FollowRequestSerializer(followRequest, many=False)
                elif n.notification_type == "like_post":
                    like = LikePost.objects.get(like_id=n.notification_id)
                    result = LikePostSerializer(like, many=False)
                elif n.notification_type == "like_comment":
                    like = LikeComment.objects.get(like_id=n.notification_id)
                    result = LikeCommentSerializer(like, many=False)
                elif n.notification_type == "comment":
                    comment = Comment.objects.get(id=n.notification_id)
                    result = CommentSerializer(comment, many=False)
                else:
                    return response.Response(f"Error getting notifcations, invalid notifcation {n} saved in the DB", status.HTTP_500_INTERNAL_SERVER_ERROR)
                items.append(result)

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
            notifcation: Notification = Notification.objects.create(author=author)
            notification_type = request.data['type']
            notifcation_id = request.data['id']

            if(notification_type != "post" and notification_type != "follow_request" and
            notification_type != "like_post" and  notification_type != "like_comment" and notification_type != "comment"):
                return response.Response(f"Post Inbox Error: Invalid notifcation type: {notification_type}", status=status.HTTP_400_BAD_REQUEST)

            notifcation.notification_type = notification_type
            notifcation.notification_id = notifcation_id
            notifcation.save()
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
