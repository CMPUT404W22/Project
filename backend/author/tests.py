from author.models import Author
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class AuthorTestCase(APITestCase):

    def setUp(self):
        # create users
        Author.objects.create_user(username="test1", password="password",
                                   display_name="test1", github="0")

        Author.objects.create_user(username="user1", password="password",
                                   display_name="user1", github="1")

        Author.objects.create_user(username="user2", password="password",
                                   display_name="user2", github="2")

        # get the ids of the users
        self.author1 = Author.objects.get(username="user1")
        self.foreignId1 = self.author1.id

        self.author2 = Author.objects.get(username="user2")
        self.foreignId2 = self.author2.id

        self.user = Author.objects.get(username="test1")
        self.id = self.user.id

        # Authenticate user
        self.client = APIClient()
        self.client.login(username='test1', password='password')