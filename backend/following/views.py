from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView

from author.models import Author
from following.models import Following


class GetFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, user_id):
        # gets a list of authors who are user_id's followers
        try:
            author = Author.objects.get(id=user_id)
            followers = Following.objects.filter(following=author)
            result = {
                "type": "followers",
                "items": [follower.author.toJson() for follower in followers]
            }
            return response.Response(result, status.HTTP_200_OK)

        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

class EditFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def delete(self, request, user_id, foreign_user_id):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHORs_ID
        try:
            follower = Author.objects.get(id=foreign_user_id)
            author = Author.objects.get(id=user_id)
            record = Following.objects.get(author=follower, following=author)
            record.delete()
            return response.Response("Deleted", status.HTTP_200_OK)
        except Exception as e:
            return response.Response("Error while trying to delete", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id, foreign_user_id):
        # Add FOREIGN_AUTHOR_ID as follower of AUTHOR_ID
        try:
            author = Author.objects.get(id=user_id)
            follower = Author.objects.get(id=foreign_user_id)
            Following.objects.create(author=follower, following=author)
            return response.Response("Added", status.HTTP_200_OK)
        except Exception as e:
            return response.Response("Error while trying to add", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, user_id, foreign_user_id):
        # check if FOREIGN_AUTHOR_ID is a follower of AUTHOR_ID
        try:
            author = Author.objects.get(id=user_id)
            unfollower = Author.objects.get(id=foreign_user_id)
            followers = Following.objects.filter(following=author)
            if followers:
                for follower in followers:
                    if follower.author == unfollower:
                        return response.Response("True", status.HTTP_200_OK)

            return response.Response("False", status.HTTP_200_OK)
        except Exception as e:
            return response.Response("Error while trying to get followers", status=status.HTTP_400_BAD_REQUEST)


class FollowingApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request):
        pass


def test(request, author_username):
    followers = Following.objects.all()
    return HttpResponse(str(followers))


def addFollower(request):
    # 'service/authors/{AUTHOR_ID}/addFollower/'
    pass


def removeFollower(request):
    # 'service/authors/{AUTHOR_ID}/removeFollower/'
    pass


def addFollowing():
    # 'service/authors/{AUTHOR_ID}/addFollowing/'
    pass


def removeFollowing():
    # 'service/authors/{AUTHOR_ID}/removeFollowing/'
    pass
