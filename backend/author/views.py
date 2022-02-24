from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
import json
from author.models import MyUserManager, Author

'''
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
'''


class GetAuthorsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request):
        users = Author.objects.filter(is_staff=False)

        if len(request.query_params) != 0:
            page = request.query_params["page"]
            size = 10
            try:
                size = request.query_params["size"]
            except Exception as _:
                pass

            paginator = Paginator(users, size)
            page_obj = paginator.get_page(page)

            result = {
                "type": "authors",
                "items": [user.toJson() for user in page_obj]
            }

            return response.Response(result, status=status.HTTP_200_OK)
        else:
            result = {
                "type": "authors",
                "items": [user.toJson() for user in users]
            }

            return response.Response(result, status=status.HTTP_200_OK)


class GetAuthorApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, user_id):
        try:
            user = Author.objects.get(id=user_id, is_staff=False)

            return response.Response(user.toJson(), status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        try:
            if str(request.user.id) == user_id or request.user.is_staff:
                display_name = request.data["displayName"]
                github = request.data["github"]
                profile_image = request.data["profileImage"]

                user = Author.objects.get(id=user_id)
                user.display_name = display_name
                user.github = github
                user.image = profile_image
                user.save()

                return response.Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return response.Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class GetAuthorFollowersApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, user_id):
        pass
