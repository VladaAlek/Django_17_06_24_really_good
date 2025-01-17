from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Bibliography
from .forms import ReviewForm, BibliographyForm, DeleteForm


# Class-based views

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
            messages.add_message(request, messages.SUCCESS, 'Summary saved successfully', extra_tags='about')
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


def book_detail(request, bibliography_id):
    
    '''
    Display an individual :model:`book.Bibliography`.

    **Context**

    ``bibliography``
        An instance of :model:`book.Bibliography`.

    ``reviews``
        all reviews related to the same bibliography`.

    ``reviews_count``
        variable that stores the number of reviews count`.

    **Template:**

    :template:`book/review_detail.html`
    shows single bibliography view and all related reviews

    '''
    
    bibliography = get_object_or_404(Bibliography, pk=bibliography_id)
    reviews = bibliography.reviews.all().order_by("-created_on")
    reviews_count = bibliography.reviews.count()
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.bibliography = bibliography
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted', extra_tags='review')
            return redirect('book_detail', bibliography_id=bibliography_id)
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
        {
        "bibliography": bibliography,
        "reviews": reviews,
        "reviews_count": reviews_count,
        "review_message": review_message,
        }
        
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


def review_edit(request, bibliography_id, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Bibliography.objects.all()
        bibliography = get_object_or_404(queryset, pk=bibliography_id)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)  

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.user = request.user
            review.bibliography = bibliography
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Review!')

        return HttpResponseRedirect(reverse('book_detail', args=[bibliography_id]))



def review_delete(request, bibliography_id, review_id):
    """
    view to delete review
    """
    
    queryset = Bibliography.objects.all()
    bibliography = get_object_or_404(queryset, pk=bibliography_id)
    review = get_object_or_404(Review, pk=review_id)
    

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('book_detail', args=[bibliography_id]))