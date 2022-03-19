import base64

from django.core.files.base import ContentFile
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView

from author.models import Author
from author.serializer import AuthorSerializer
from comment.models import Comment
from comment.serializer import CommentSerializer
from notification.models import Notification
from post.models import Post
from post.serializer import PostSerializer

# region authors
from following.models import Following


class GetAuthorsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request):
        """
        Get Authors
        """
        users = Author.objects.all()

        result = {
            "type": "authors",
            "items": self.serializer_class(users, many=True).data
        }

        return response.Response(result, status=status.HTTP_200_OK)


class GetAuthorApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request, id):
        """
        Get Author
        """
        user = Author.objects.get(id=id)
        result = self.serializer_class(user, many=False)
        return response.Response(result.data, status=status.HTTP_200_OK)
# endregion


# region followings
class GetFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request, author_id):
        try:
            author = Author.objects.get(id=author_id)
            followers = [x.author for x in Following.objects.filter(following=author)]

            result = {
                "type": "followers",
                "items": AuthorSerializer(followers, many=True).data
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class CheckFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request, author_id, follower_id):
        try:
            author = Author.objects.get(id=author_id)
            isFollower = Author.objects.get(id=follower_id)
            followers = Following.objects.filter(following=author)
            for follower in followers:
                if follower.author == isFollower:
                    return response.Response("True", status.HTTP_200_OK)
            return response.Response("False", status.HTTP_200_OK)
        except Exception as e:
            return response.Response(f"Error while trying to get followers: {e}", status=status.HTTP_400_BAD_REQUEST)
# endregion


# region posts
class GetPostsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = PostSerializer

    def get(self, request, author_id):
        post = Post.objects.filter(author=author_id)

        result = {
            "type": "posts",
            "items": self.serializer_class(post, many=True).data
        }

        return response.Response(result, status=status.HTTP_200_OK)


class GetPostApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = PostSerializer

    def get(self, request, author_id, post_id):
        try:
            post = Post.objects.get(id=post_id)
            result = self.serializer_class(post, many=False).data

            return response.Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_404_NOT_FOUND)


class GetPostImageApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = PostSerializer

    def get(self, request, author_id, post_id):
        post = Post.objects.get(id=post_id)

        if post.type == "image/png;base64" or post.type == "image/jpeg;base64":
            format = "png" if "png" in post.type else "jpeg"
            img_str = post.content

            data = ContentFile(base64.b64decode(img_str), name='temp.' + format)  # You can save this as file instance.
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
# endregion


# region comments
class GetCommentsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = CommentSerializer

    def get(self, request, author_id, post_id):
        comments = Comment.objects.filter(author=author_id, post=post_id)

        result = {
            "type": "comments",
            "post": f'http://127.0.0.1:8000/authors/{author_id}/posts/{post_id}/',
            "id": f'http://127.0.0.1:8000/authors/{author_id}/posts/{post_id}/comments',
            "comments": self.serializer_class(comments, many=True).data
        }

        return response.Response(result, status=status.HTTP_200_OK)
# endregion


# region likes

# endregion


# region liked

# endregion


# region inbox
class SendToInboxApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = None

    def post(self, request, author_id):
        author = Author.objects.get(id=author_id)
        try:
            notification: Notification = Notification.objects.create(author=author)
            notification_type = request.data['type']
            notification_id = request.data['id']

            if (notification_type != "post" and
                    notification_type != "follow_request" and
                    notification_type != "like_post"
                    and notification_type != "like_comment"
                    and notification_type != "comment"):
                return response.Response(f"Post Inbox Error: Invalid notifcation type: {notification_type}", status=status.HTTP_400_BAD_REQUEST)

            notification.notification_type = notification_type
            notification.notification_id = notification_id
            notification.save()
            return response.Response("Added notification", status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response(f"Failed to post to inbox: {e}", status=status.HTTP_400_BAD_REQUEST)

# endregion

