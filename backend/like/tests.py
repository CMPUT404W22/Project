import json
import uuid

from django.db import transaction

from author.models import Author
from post.models import Post
from comment.models import Comment
from notification.models import Notification
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class LikesTestCase(APITestCase):

    def setUp(self):
        # create users
        Author.objects.create_user(username="test1", password="password",
                                   display_name="test1", github="0")

        Author.objects.create_user(username="user1", password="password",
                                   display_name="user1", github="1")

        Author.objects.create_user(username="user2", password="password",
                                   display_name="user2", github="2")

        # get the ids of the users
        self.authorname1 = Author.objects.get(username="user1")
        self.foreign_id1 = self.authorname1.id

        self.authorname2 = Author.objects.get(username="user2")
        self.foreign_id2 = self.authorname2.id

        self.username = Author.objects.get(username="test1")
        self.id = self.username.id

        # Authenticate users
        self.user = APIClient()
        self.user.login(username='test1', password='password')

        self.author1 = APIClient()
        self.author1.login(username='test1', password='password')

        self.author2 = APIClient()
        self.author2.login(username='test1', password='password')

    def create_post(self, author_name):
        post = Post.objects.create(
            id=uuid.uuid4(),
            author=author_name,
            type=0,
            title="Test Post",
            description="Testing",
            content="Testing posting!",
            visibility=0,
            unlisted="False",
            categories="Test"
        )
        return post

    def create_comment(self,author_name, post):
        comment = Comment.objects.create(
            id=uuid.uuid4(),
            author=author_name,
            post=post,
            content="That is a nice picture!",
            type="comment"
        )
        return comment

    def test_get_posts_likes(self):
        # testing get a list of likes from other authors on author id’s post post_id

        #author2 likes users post
        post = self.create_post(self.username)
        like_data = {"type": "like_post", "id": post.id}
        self.author2.post(f'/service/authors/{self.foreign_id2}/inbox', like_data, format='json')

        #get the list of people who liked users post
        response = self.user.get(f'/service/authors/{self.id}/posts/{post.id}/likes', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_comment_likes(self):
        # testing getting a list of likes from other authors on AUTHOR_ID’s post POST_ID comment COMMENT_ID
        # author1 makes a comment
        post = self.create_post(self.username)
        comment = self.create_comment(self.authorname1, post)

        # author2 and user likes author1's comment
        like_data = {"type": "like_comment", "id": comment.id}
        with transaction.atomic():
            self.author2.post(f'/service/authors/{self.foreign_id2}/inbox', like_data, format='json')
            self.user.post(f'/service/authors/{self.id}/inbox', like_data, format='json')

            # get the people who liked the comment
            response = self.user.get(f'/service/authors/{self.id}/posts/{post.id}/comments/{comment.id}/likes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2, "Did not add both into the list")

    def test_liked(self):
        # tests getting a list of likes originating from the author
        post = self.create_post(self.authorname2)
        like_data = {"type": "like_post", "id": post.id}
        # have user like author2 post
        self.user.post(f'/service/authors/{self.id}/inbox', like_data, format='json')
        # have author1 like author2 post
        self.author1.post(f'/service/authors/{self.foreign_id1}/inbox', like_data, format='json')

        # get the list of likes that user1 made
        response = self.user.get(f'/service/authors/{self.id}/liked')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

        # have author1 and author2 make a comment on author2's post
        comment = self.create_comment(self.authorname1, post)
        comment2 = self.create_comment(self.authorname2, post)

        # have user like author1's comment
        like_comment = {"type": "like_comment", "id": comment.id}
        like_comment2 = {"type": "like_comment", "id": comment2.id}
        self.user.post(f'/service/authors/{self.id}/inbox', like_comment, format='json')
        self.user.post(f'/service/authors/{self.id}/inbox', like_comment2, format='json')

        response = self.user.get(f'/service/authors/{self.id}/liked')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_not_liked_posts(self):
        # test trying to get likes on post that hasnt been liked
        # have author1 create a post
        post = self.create_post(self.authorname1)

        # test when user did not like the post
        response = self.author1.get(f'/service/authors/{self.foreign_id1}/posts/{post.id}/likes', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        # test when getting likes to a post that hasnt been create by that user
        response = self.user.get(f'/service/authors/{self.id}/posts/{post.id}/likes', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_not_liked_comment(self):
        # test trying to get likes on comment that has not been liked
        # have author1 create a post
        post = self.create_post(self.authorname1)
        comment = self.create_comment(self.authorname2, post)

        response = self.user.get(f'/service/authors/{self.id}/posts/{post.id}/comments/{comment.id}/likes')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


