from django.core.paginator import Paginator
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView

from author.models import Author
from following.models import Following

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
        users = Author.objects.all()

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
            user = Author.objects.get(id=user_id)

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
        followers = Following.objects.filter(following=user_id)

        result = {
            "type": "followers",
            "items": [follower.author.toJson() for follower in followers]
        }

        return response.Response(result, status.HTTP_200_OK)

    def delete(self, request, user_id, foreign_user_id):
        # remove FOREIGN_AUTHOR_ID as a follower of AUTHORs_ID
        follower = Author.objects.get(id=foreign_user_id)
        author = Author.objects.get(id=user_id)
        record = Following.objects.get(author=follower, following=author)
        record.delete()
        return response.Response("Deleted", status.HTTP_200_OK)

    def put(self, request, user_id, foreign_user_id):
        # Add FOREIGN_AUTHOR_ID as follower of AUTHOR_ID
        author = Author.objects.get(id=user_id)
        follower = Author.objects.get(id=foreign_user_id)
        Following.objects.create(author=follower, following=author)
        return response.Response("Added", status.HTTP_200_OK)

    def get(self, request, user_id, foreign_user_id):
        # check if FOREIGN_AUTHOR_ID is a follower of AUTHOR_ID
        author = Author.objects.get(id=user_id)
        followers = Following.objects.filter(following=author)
        if followers:
            for follower in followers:
                if follower.id == foreign_user_id:
                    return response.Response("True", status.HTTP_200_OK)

        return response.Response("False", status.HTTP_200_OK)
