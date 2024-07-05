from django.shortcuts import render
from django.views import generic
from .models import Review
#from django.http import HttpResponse

# Create your views here.
#def my_book(request):
    #return HttpResponse("Hello, this Book app's page")

class ReviewList(generic.ListView):
    #model = Review
    queryset = Review.objects.all()
    template_name = "review_list.html"