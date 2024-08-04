from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Review, Bibliography
from .forms import ReviewForm, SummaryForm, BibliographyForm

# Create your views here.

# Class-based views

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "book/index.html"
    paginate_by = 6


class ReviewList(generic.ListView):
    queryset = Bibliography.objects.all()
    template_name = "book/index.html"
    paginate_by = 6


# Function-based views

def about(request):
    if request.method == "POST":
        summary_form = BibliographyForm(request.POST)
        if summary_form.is_valid():
            new_summary = summary_form.save(commit=False)
            new_summary.reader = request.user
            new_summary.save()
            messages.success(request, "New bibliographical entry submitted", extra_tags="about")
            return redirect("about")
    else:
        summary_form = BibliographyForm()


    # Filter messages to pass only one 'about' message

    about_message = None

    for message in messages.get_messages(request):

        if 'about' in message.tags:

            about_message = message

            break

    return render(request, "book/about.html", {
        "summary_form": summary_form,
        "about_message": about_message,     
        }
        )




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

def review_edit(request, review_id):
    """
    view to edit reviews 
    """

    # retrive object from db based on review id
    review = get_object_or_404(Review, review_id)

    if request.method == "POST":

        # creates an instance of 'ReviewForm' with the sumbitted data
        review_form = ReviewForm(data=request.POST, instance=review)

            
        # check condition: user is the author of the review, user is loged in
        if review_form.is_valid() and review.user == request.user:
            review_form.save()
            messages.add_message(request. messages.SUCCESS, "Error updating review!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")
    # checked condition failed: returnt the original instance
    else:
        review_form = ReviewForm(instance=review)

    # renders review_detail page
    return HttpResponseRedirect(reverse('review_detail'))


#return HttpResponseRedirect(reverse('post_detail', args=[review.id]))


def comment_delete(request, review_id):
    """
    view to delete comment
    """
    
    review = get_object_or_404(Review, review_id)
    

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))