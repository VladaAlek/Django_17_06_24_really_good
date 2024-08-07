from .models import Review, Bibliography
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =('content',)


class BibliographyForm(forms.ModelForm):
    class Meta:
        model = Bibliography
        fields = ['title', 'author', 'publisher', 'year', 'edition', 'summary']
        labels = {
            'title': 'Title',
            'author': 'Author(s)',
            'publisher': 'Publisher',
            'year': 'Year',
            'edition': 'Edition (Optional)',
            'summary': 'Summary',
        }




class SummaryForm(forms.ModelForm):
    class Meta:
       model = Bibliography
       fields = ('summary',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)