from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    
class Bibliography(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    edition = models.IntegerField(blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="books", blank=True, null=True)



