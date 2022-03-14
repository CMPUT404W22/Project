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
from post.serializer import PostSerializer
from like.serializer import LikePostSerializer, LikeCommentSerializer
from comment.serializer import CommentSerializer

# Create your views here.
class NotificationsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    post_serializer = PostSerializer

    def get(self, request, user_id):
        # gets a list of authors who are user_id's followers
        try:
            author = Author.objects.get(id=user_id)
            notifications = Notification.objects.filter(author=author)

            items = list()

            for n in notifications:
                result = None
                if n.notification_type == "post":
                    post = Post.objects.filter(id=n.notification_id)
                    result = PostSerializer(post, many=False)
                elif n.notification_type != "follow":
                    pass
                elif n.notification_type != "like_post":
                    like = LikePost.objects.filter(like_id=n.notification_id)
                    result = LikePostSerializer(like, many=False)
                elif n.notification_type != "like_comment":
                    like = LikeComment.objects.filter(like_id=n.notification_id)
                    result = LikeCommentSerializer(like, many=False)
                elif notification_type != "comment":
                    comment = Comment.objects.filter(id=n.notification_id)
                    result = CommentSerializer(comment, many=False)
                else:
                    return response.Response(f"Error getting notifcations, invalid notifcation {n} saved in DB", status.HTTP_500_INTERNAL_SERVER_ERROR)
                items.append(result)

            result = {
                "type": "inbox",
                "items": [i.content.toJson() for i in items]
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, user_id):
        author = Author.objects.get(id=user_id)

        try:
            notifcation = Notification.objects.create(author=author)
            notifcation_type = request.data["type"]
            notifcation_id = request.data["id"]

            if(notification_type != "post" or notification_type != "follow" or
            notification_type != "like_post" or  notification_type != "like_comment" or notification_type != "comment"):
                return response.Response(f"Post Inbox Error: Invalid notifcation type", status=status.HTTP_400_BAD_REQUEST)

            notifcation.notifcation_type = notifcation_type
            notifcation.notification_id = notifcation_id
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
