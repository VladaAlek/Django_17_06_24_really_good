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


def review_detail(request, slug):
    """
    Display an individual :model:`book.Review`.

    **Context**

    ``review``
        An instance of :model:`book.Review`.

    **Template:**

    :template:`book/review_detail.html`
    """

    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "book/review_detail.html",
        {"review": review},
    )
