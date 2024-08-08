from django.test import TestCase
from .forms import CommentForm, ReviewForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())


class TestReviewForm(TestCase):

    def test_form_is_not_valid(self):
        comment_form = CommentForm({'content': 'This is a great post'})
        self.assertFalse(comment_form.is_valid())