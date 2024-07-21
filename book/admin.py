from django.contrib import admin
from .models import Bibliography, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')
    search_fields = ['title', 'author']
    list_filter = ('year',)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('bibliography', 'user', 'created_on')
    search_fields = ['user__username', 'bibliography__title']
    list_filter = ('created_on',)
    summernote_fields = ('content',)

