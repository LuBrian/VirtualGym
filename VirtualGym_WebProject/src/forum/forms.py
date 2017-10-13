from django import forms
from .models import Questions

class QuestionsForm(forms.ModelForm):
    questionDescription = forms.CharField()
    class Meta:
        model=Questions
        # fields={"exerciseDescription","exerciseTag"}
        fields={"questionDescription"}
