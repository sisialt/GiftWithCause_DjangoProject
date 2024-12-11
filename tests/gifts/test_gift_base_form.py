from django.test import TestCase

from GiftWithCause_DjangoProject.gifts.forms import GiftBaseForm


class TestGiftBaseForm(TestCase):
    def setUp(self):
        self.gift = {
            'title': 'Gift title',
            'image': 'https://someimage.com',
            'description': 'This is a description longer than 30 chars',
            'price': 2.5,
        }

    def test__form_is_valid__expect_true(self):
        form = GiftBaseForm(data=self.gift)
        self.assertTrue(form.is_valid())

    def test__form_is_invalid__short_title__expect_custom_error(self):
        self.gift['title'] = 'No'

        form = GiftBaseForm(data=self.gift)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(
            form.errors['title'][0],
            "Title must be at least 3 characters long."
        )

    def test__form_is_invalid__short_description__expect_custom_error(self):
        self.gift['description'] = 'Too short'

        form = GiftBaseForm(data=self.gift)

        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)
        self.assertEqual(
            form.errors['description'][0],
            "Description must be at least 30 characters long."
        )

    def test__form_is_invalid__missing_required_fields(self):
        self.gift = {}

        form = GiftBaseForm(data=self.gift)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('image', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('price', form.errors)

