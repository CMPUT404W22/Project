from author.models import Author
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
        self.foreignId1 = self.author1.id

        self.authorname2 = Author.objects.get(username="user2")
        self.foreignId2 = self.author2.id

        self.username = Author.objects.get(username="test1")
        self.id = self.user.id

        # Authenticate users
        self.user = APIClient()
        self.user.login(username='test1', password='password')

        self.author1 = APIClient()
        self.author1.login(username='test1', password='password')

        self.author2 = APIClient()
        self.author2.login(username='test1', password='password')

    def test_post(self):
        # testing post to like object to author_id
        #TODO: have author1 make a post
        # have author2 like author1 post
        # check if liked object was sent to author1
        pass

    def test_get_post_likes(self):
        # testing get a list of likes from other authors on author id’s post post_id
        #TODO: have user create another post, have author1 and author2 like the post
        # check if the list of likes has a length of 2
        #response = self.client.put(f'/service/authors/{self.id}/posts/{self.postId}/likes')
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass

    def test_get_comment_likes(self):
        # testing getting a list of likes from other authors on AUTHOR_ID’s post POST_ID comment COMMENT_ID
        #TODO: have user create a post, and author1 comment on the post, and author2 like the post
        #self.client.put(f'/service/authors/{self.id}/posts/{self.postId}/comments/{self.commentId}/likes')
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass