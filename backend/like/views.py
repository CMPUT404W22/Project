from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from author.models import Author
from like.models import LikePost, LikeComment
from like.serializer import LikePostSerializer, LikeCommentSerializer
from post.models import Post
from comment.models import Comment
from itertools import chain


class GetLikeApiView(GenericAPIView):
    authentication_classes = []
    serializer_class = LikePostSerializer

    def post(self, request, user_id):
        # send a like object to AUTHOR_ID
        pass

    def get(self, request, user_id, post_id):
        # gets a list of likes from other authors on AUTHOR_ID’s post POST_ID
        try:
            post = Post.objects.get(id=post_id, author=user_id)
            likes = LikePost.objects.filter(post=post)
            return response.Response(self.serializer_class(likes, many=True).data, status=status.HTTP_200_OK)

        except Exception as e:
            return response.Response(f"Error occurred: {e}", status.HTTP_400_BAD_REQUEST)


class GetLikeCommentApiView(GenericAPIView):
    authentication_classes = []
    serializer_class = LikeCommentSerializer

    def get(self, request, user_id, post_id, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            likes = LikeComment.objects.filter(comment=comment)
            return response.Response(self.serializer_class(likes, many=True).data, status=status.HTTP_200_OK)

        except Exception as e:
            return response.Response(f"Error occurred: {e}", status.HTTP_400_BAD_REQUEST)


class GetLikedApiView(GenericAPIView):
    authentication_classes = []
    serializer_class_post = LikePostSerializer
    serializer_class_comment = LikeCommentSerializer

    def get(self, request, user_id):
        # gets posts and comment objects that the author likes
        try:
            author = Author.objects.get(id=user_id)
            liked_post = LikePost.objects.filter(author=author)
            liked_comment = LikeComment.objects.filter(author=author)

            result = self.serializer_class_post(liked_post, many=True).data + self.serializer_class_comment(liked_comment, many=True).data

            return response.Response(self.serializer_class_post(result, many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(f"Error: {e}", status.HTTP_400_BAD_REQUEST)