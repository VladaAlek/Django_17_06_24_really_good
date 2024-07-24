from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

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

    **Template:**

    :template:`book/review_detail.html`
    """

    queryset = Review.objects.all()
    review = get_object_or_404(queryset, id=review_id)

    return render(
        request,
        "book/review_detail.html",
        {"review": review},
    )
