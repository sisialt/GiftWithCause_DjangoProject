from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator
from GiftWithCause_DjangoProject.gifts.models import Gift

UserModel = get_user_model()


class TestGiftCreateView(TestCase):
    def setUp(self):
        self.user_creator = UserModel.objects.create_user(
            email='creator@test.com',
            password='password',
            is_creator=True,
        )

        self.creator = GiftCreator.objects.get(user=self.user_creator)

        self.user_not_creator = UserModel.objects.create_user(
            email='nocreator@test.com',
            password='password',
            is_creator=False,
        )

        self.gift = {
            'title': 'Gift title',
            'image': 'https://someimage.com',
            'description': 'This is a description longer than 30 chars',
            'price': 2.5,
        }

    def test__forbidden_if_not_logged_in(self):
        response = self.client.get(reverse('gift-create'))

        self.assertEqual(response.status_code, 403)

    def test__forbidden_if_logged_in_but_not_creator(self):
        self.client.login(email='nocreator@test.com', password='password')

        response = self.client.get(reverse('gift-create'))

        self.assertEqual(response.status_code, 403)

    def test__logged_in_creator_successful(self):
        self.client.login(email='creator@test.com', password='password')

        response = self.client.get(reverse('gift-create'))

        self.assertEqual(response.status_code, 200)

    def test__form_invalid_when_profile_incomplete(self):
        self.client.login(email='creator@test.com', password='password')

        response = self.client.post(reverse('gift-create'), data=self.gift)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "You must complete your profile information before creating a gift."
        )

    def test__form_valid_for_valid_gift__expect_gift_is_created_and_redirect_to_gift_details(self):
        self.user_creator.profile.first_name = 'First'
        self.user_creator.profile.save()

        self.client.login(email='creator@test.com', password='password')

        response = self.client.post(reverse('gift-create'), data=self.gift)

        gift = Gift.objects.filter(title='Gift title').first()
        self.assertIsNotNone(gift)

        expected_url = reverse('gift-details', kwargs={'pk': gift.pk})
        self.assertRedirects(response, expected_url)
