from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review
from .forms import ReviewForm

# Create your views here.

# Class-based views

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "book/index.html"
    paginate_by = 6


# Function-based views

def about(request):
    return render(request, 'book/about.html')


def review_detail(request, review_id):
    """
    Display an individual :model:`book.Review`.

    **Context**

    ``review``
        An instance of :model:`book.Review`.

    ``reviews``
        all reviews related to the same bibliography`.

    ``reviews_count``
        variable that stores the number of reviews count`.

    **Template:**

    :template:`book/review_detail.html`
    """

    queryset = Review.objects.all()
    review = get_object_or_404(queryset, id=review_id)
    reviews = Review.objects.filter(bibliography=review.bibliography).order_by("-created_on")
    reviews_count = reviews.count()
    reviews_form = ReviewForm()

    return render(
        request,
        "book/review_detail.html",
        {"review": review,
        "reviews": reviews,
        "reviews_count": reviews_count,
        "reviews_form": reviews_form,
        },
        
    )
