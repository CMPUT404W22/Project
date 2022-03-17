from ast import Import
from urllib import response
from post.models import Post
from author.models import Author
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class FollowersTestCase(APITestCase):

    def setUp(self):
        # create users
        Author.objects.create_user(username="test1", password="password",
                                   display_name="test1", github="0")
        
        Author.objects.create_user(username="user1", password="password",
                                   display_name="user1", github="1")

        # get the ids of the users
        self.user = Author.objects.get(username="test1")
        self.id = self.user.id
        
        self.author1 = Author.objects.get(username="user1")
        self.foreignId1 = self.author1.id
        
        # create a post 
        self.post = Post.objects.create(
            id=self.id, 
            author = self.user,
            type = 0,
            title = "TheTitle",
            description = "TheDescription",
            content = "Nice Day!",
            visibility = 0,
            unlisted = False,
            categories = "Nice"
        )

        # Authenticate user
        self.client = APIClient()
        self.client.login(username='test1', password='password')

    def test_get_post(self):
        # test getting/creating/updating/posting posts
        response = self.client.get(f'/service/authors/{self.id}/posts/{self.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.id, self.id)
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.type, 0)
        self.assertEqual(self.post.title, "TheTitle")
        self.assertEqual(self.post.description, "TheDescription")
        self.assertEqual(self.post.content, "Nice Day!")
        self.assertEqual(self.post.visibility, 0)
        self.assertEqual(self.post.unlisted, False)
        self.assertEqual(self.post.categories, "Nice")

    def test_delete_posts(self):
        # test deleting a post
        response = self.client.delete(f'/service/authors/{self.id}/posts/{self.id}')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.content, b'"Deleted"')
        
    def test_invalid_delete(self):
        # test when trying to delete follower that isnt in database
        response = self.client.delete(f'/service/authors/{self.id}/posts/{self.foreignId1}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_put(self):
        # test when uses an id that is not valid
        invalidId = "123"
        response = self.client.delete(f'/service/authors/{self.id}/posts/{invalidId}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_get(self):
        # test when uses an id that is not valid
        invalidId = "123"
        response = self.client.delete(f'/service/authors/{self.id}/posts/{invalidId}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
