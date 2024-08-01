from .models import Review, Bibliography
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =('content',)

#class ContributeForm(forms.ModelForm):
    #class Meta:
       # model = Bibliography
       # fields =('summary',)