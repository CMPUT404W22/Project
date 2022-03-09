from django.shortcuts import render
from .models import Following
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from author.models import Author
from author.serializer import AuthorSerializer
from following.models import Following


class GetFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request, user_id):
        # gets a list of authors who are user_id's followers
        try:
            author = Author.objects.get(id=user_id)
            followers = [x.author for x in Following.objects.filter(following=author)]

            result = {
                "type": "followers",
                "items": AuthorSerializer(followers, many=True).data
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class EditFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def delete(self, request, user_id, foreign_user_id):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHORs_ID
        try:
            follower = Author.objects.get(id=foreign_user_id)
            author = Author.objects.get(id=user_id)
            record = Following.objects.get(author=follower, following=author)
            record.delete()
            return response.Response("Deleted", status.HTTP_202_ACCEPTED)
        except Exception as e:
            return response.Response(f"Error while trying to delete: {e}", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id, foreign_user_id):
        # Add FOREIGN_AUTHOR_ID as follower of AUTHOR_ID
        try:
            author = Author.objects.get(id=user_id)
            follower = Author.objects.get(id=foreign_user_id)
            Following.objects.create(author=follower, following=author)
            return response.Response("Added", status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response(f"Error while trying to add: {e}", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, user_id, foreign_user_id):
        # check if FOREIGN_AUTHOR_ID is a follower of AUTHOR_ID
        try:
            author = Author.objects.get(id=user_id)
            isFollower = Author.objects.get(id=foreign_user_id)
            followers = Following.objects.filter(following=author)
            for follower in followers:
                if follower.author == isFollower:
                    return response.Response("True", status.HTTP_200_OK)
            return response.Response("False", status.HTTP_200_OK)
        except Exception as e:
            return response.Response(f"Error while trying to get followers: {e}", status=status.HTTP_400_BAD_REQUEST)


# TODO: delete if unused
class GetFollowingApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def get(self, request, user_id):
        # gets a list of authors who are user_id's followers
        try:
            author = Author.objects.get(id=user_id)
            following = Following.objects.filter(author=author)
            result = {
                "type": "following",
                "items": [user.author.toJson() for user in following]
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

# TODO: delete if unused
class EditFollowingApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]
    serializer_class = AuthorSerializer

    def delete(self, request, user_id, foreign_user_id):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHORs_ID
        try:
            author = Author.objects.get(id=user_id)
            following = Author.objects.get(id=foreign_user_id)
            record = Following.objects.get(author=author, following=following)
            record.delete()
            return response.Response("Deleted", status.HTTP_200_OK)
        except Exception as e:
            return response.Response("Error while trying to delete", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id, foreign_user_id):
        # Add FOREIGN_AUTHOR_ID as follower of AUTHOR_ID
        try:
            author = Author.objects.get(id=user_id)
            following = Author.objects.get(id=foreign_user_id)
            Following.objects.create(author=author, following=following)
            return response.Response("Added", status.HTTP_200_OK)
        except Exception as e:
            return response.Response("Error while trying to add", status=status.HTTP_404_NOT_FOUND)

