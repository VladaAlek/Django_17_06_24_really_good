from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "book/index.html"
    paginate_by = 6

def about(request):
    return render(request, 'book/about.html')