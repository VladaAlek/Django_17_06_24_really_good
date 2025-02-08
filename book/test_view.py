from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Bibliography, Review
from .forms import ReviewForm

class TestReviewViews(TestCase):

    # setup user
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        # Ensures the test user is authenticated.
        self.client.login(username="myUsername", password="myPassword")

        #setup the instance of bibliography
        self.bibliography = Bibliography.objects.create(
            title="Test Book",
            author="Test Author",
            publisher="Test Publisher",
            year=2024,
            slug="test-book"
        )
        # setup the instance of review
        self.review = Review.objects.create(
            content="This is a test review",
            user=self.user,
            bibliography=self.bibliography,
            slug="test-review"
        )

    def test_render_review_detail_page_with_comment_form(self):
        response = self.client.get(reverse('book_detail', args=[self.bibliography.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertContains(response, "This is a test review")
        self.assertIsInstance(response.context["review_form"], ReviewForm)
