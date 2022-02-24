from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView

from following.models import Following


class FollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, *args, **kwargs):
        #followers = Following.objects.filter(following=request.user)
        followers = Following.objects.filter(following=1)
        list = []
        print("RAN GET")
        for e in followers:
            list.append(e)
        return HttpResponse(list)
        #return response.Response(str(followers), status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHOR_ID
        record = Following.objects.get(id=kwargs["foreign_author_id"])
        record.delete()
        return response.Response("Deleted", status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        # Add FOREIGN_AUTHOR_ID as follower of AUTHOR_ID
        author_obj = Author.objects.get()
        record = Following.objects.create(author = kwargs["foreign_author_id"], following = request.user)
        return response.Response("Added", status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        pass

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
