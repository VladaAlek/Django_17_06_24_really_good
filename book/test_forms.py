from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bibliography, Review
from .forms import ReviewForm
from django.utils.text import slugify


class TestReviewForm(TestCase):

    def setUp(self):
        """ Set up test user and bibliography instance """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.bibliography = Bibliography.objects.create(
            reader=self.user,
            title="Test Book",
            author="Test Author",
            publisher="Test Publisher",
            year=2024,
            slug=slugify("Test Book")
        )

    def test_form_is_not_valid(self):
        """ form is invalid without all required fields """
        review_form = ReviewForm(data={'content': ''})
        self.assertFalse(review_form.is_valid(), msg="I expect the test to fail")

    def test_form_is_valid(self):
        """ form is valid with all required fields """
        review_form = ReviewForm(data={
            'content': 'This is a great post',
            'user': self.user.id, 
            'bibliography': self.bibliography.id
        })
        self.assertTrue(review_form.is_valid(), msg="I expect the test to pass")
