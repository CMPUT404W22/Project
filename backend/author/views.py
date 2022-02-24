from django.shortcuts import render
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
import json
from author.models import MyUserManager, Author


class Register(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        profile_header = request.data["profile_header"]

        new_user = Author.objects.create_user(username, password, first_name=first_name, last_name=last_name, profile_header=profile_header)

        return response.Response(str(new_user), status=status.HTTP_200_OK)


class Authors(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, username):
        user = Author.objects.get(username=username)

        return response.Response(str(user), status=status.HTTP_200_OK)


