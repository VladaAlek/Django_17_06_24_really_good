from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Review, Bibliography
from .forms import ReviewForm, SummaryForm

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

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.bibliography = review.bibliography
            new_review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted', extra_tags='review')
            return redirect('review_detail', review_id=review.id)
    else:
        review_form = ReviewForm()

    # Filter messages to pass only one 'review' message

    review_message = None

    for message in messages.get_messages(request):

        if 'review' in message.tags:

            review_message = message

            break

    return render(
        request,
        "book/review_detail.html",
        {"review": review,
        "reviews": reviews,
        "reviews_count": reviews_count,
        "reviews_form": reviews_form,
        "review_message": review_message,
        },
        
    )


def create_summary(request):
    
    """

    **Context**

    ``summary`` 
    an instance of model: `book.Bibliography`

    ``summaries`` 
    all summaries related to the same bibliography

    **Template:**

    :template:`book/index.html`

    """
    

    if request.method == "POST":
        summary_form = SummaryForm(data=request.Post)
        if summary_form.is_valid():
            new_summary = summary_form.save(commit=False)
            new_summary.user = request.user
            new_summary.save()
            messages.add_message(request, messages.SUCCESS, 'Summary submitted', extra_tags='summary')
            return redirect('index')
        else:
            summary_form = SummaryForm()
    
 
   #Filter messages to pass only one 'review' message

    
    summary_message = None

    for message in messages.get_messages(request):

        if 'summary' in message.tags:

            summary_message = message

            break

    summaries = Bibliography.objects.all()

    return render(
        request,
        
        "book/index.html",
        {
            "summaries": summaries,
            "summary_form" : summary_form,
            "summary_message": summary_message,
        },

    )

#queryset = Bibliography.objects(all)
    #bibliography = get_object_or_404(queryset, summaries=bibliography_summary)
    #summaries  Bibliography.objects.filter(bi)