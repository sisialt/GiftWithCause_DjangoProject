from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator
from GiftWithCause_DjangoProject.gifts.models import Gift

UserModel = get_user_model()


class TestGiftEditView(TestCase):
    def setUp(self):
        self.user_creator = UserModel.objects.create_user(
            email='creator@test.com',
            password='password',
            is_creator=True
        )

        self.user_not_creator = UserModel.objects.create_user(
            email='nocreator@test.com',
            password='password',
            is_creator=False
        )

        self.superuser = UserModel.objects.create_superuser(
            email='admin@test.com',
            password='password',
            is_creator=True
        )

        self.creator = GiftCreator.objects.get(user=self.user_creator)

        self.gift = Gift.objects.create(
            title='Gift title',
            image='https://someimage.com',
            description='This is a description longer than 30 chars',
            price=2.5,
            creator=self.creator,
        )

        self.edit_url = reverse('gift-edit', kwargs={'pk': self.gift.pk})

        self.valid_edit_data = {
            'title': 'Edited Gift Title',
            'image': 'https://someimage.com',
            'description': 'This is the updated description longer than 30 chars',
            'price': 2.5,
        }

    def test__forbidden_for_no_creator_user(self):
        self.client.login(email='nocreator@test.com', password='password')

        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, 403)

    def test__superuser_can_access_edit_page(self):
        self.client.login(email='admin@test.com', password='password')

        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gift-edit.html')

    def test__successful_edit_by_creator(self):
        self.client.login(email='creator@test.com', password='password')

        response = self.client.post(self.edit_url, data=self.valid_edit_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('gift-details', kwargs={'pk': self.gift.pk}))

        self.gift.refresh_from_db()

        self.assertEqual(self.gift.title, 'Edited Gift Title')
        self.assertEqual(self.gift.description, 'This is the updated description longer than 30 chars')
        self.assertEqual(self.gift.price, 2.5)

    def test__invalid_edit_data(self):
        self.client.login(email='creator@test.com', password='password')

        invalid_data = self.valid_edit_data.copy()
        invalid_data['title'] = ''

        response = self.client.post(self.edit_url, data=invalid_data)

        self.assertFormError(response, 'form', 'title', 'Title field is required!')

        self.gift.refresh_from_db()

        self.assertEqual(self.gift.title, 'Gift title')

