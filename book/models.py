from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Bibliography(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reader_account", null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    edition = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)


    
class Review(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=True)
    bibliography = models.ForeignKey(Bibliography, on_delete=models.CASCADE, related_name="reviews", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review for {self.bibliography.title} written by {self.bibliography.author} created on {self.created_on}"


    

    



