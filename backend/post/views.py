from hashlib import new
from turtle import pos
from django.shortcuts import render
from django.core.paginator import Paginator
from sympy import re
from rest_framework import response, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView

from author.models import Author
from post.models import Post

class GetPostsApiView(GenericAPIView):
    authentication_classes = [BasicAuthentication, ]

    def get(self, request, user_id):

        post = Post.objects.filter(author=user_id)

        if len(request.query_params) != 0:
            page = request.query_params["page"]
            size = 10
            try:
                size = request.queryparams["size"]
            except Exception as _:
                pass

            paginator = Paginator(post, size)
            page_obj = paginator.get_page(page)

            result = {
                "type": "posts",
                "items": [post.toJson() for post in page_obj]
            }

            return response.Response(result, status=status.HTTP_200_OK)
        else:
            result = {
                "type": "posts",
                "items": [post.toJson() for post in post]
            }

            return response.Response(result, status=status.HTTP_200_OK)
    
    def post(self, request, user_id):
        author = Author.objects.get(id = user_id)
        try:
            post = Post.objects.create(author = author)
            title = request.data["title"]
            # print(title)
            description = request.data["description"]
            content = request.data["content"]
            visibility = request.data["visibility"]
            categories = request.data["categories"]
            count = request.data["count"]
            unlisted = request.data["unlisted"]
            # type = request.data["contentType"]

            post.title = title
            post.description = description
            post.content = content
            post.visibility = visibility
            post.categories = categories
            post.count = count
            post.unlisted = unlisted
            # print(post.title)
            post.save()
            return response.Response(post.toJson(), status=status.HTTP_201_CREATED)
        except Exception:
            return response.Response("Error", status=status.HTTP_400_BAD_REQUEST)