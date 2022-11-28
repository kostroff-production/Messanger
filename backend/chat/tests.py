from . import models
from django.urls import reverse
from rest_framework.test import APITestCase


class APIViewTests(APITestCase):
    def setUp(self) -> None:
        models.Person.objects.create_user(login='test', password='test')

    def test_login_view(self):
        response = self.client.post(reverse('login_url'), {'login': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_base_view(self):
        user = models.Person.objects.get(login='test')
        self.client.force_login(user=user)
        response = self.client.get(reverse('base_url', kwargs={'pk': user.pk}))
        arr_keys = ['person', 'permission', 'unread_chats', 'chats', 'friends', 'count_possible', 'users']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.data.keys()), arr_keys)







