from django import forms
from .models import Questions

class QuestionsForm(forms.ModelForm):
    questionDescription = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Your Answer...",
        }
    ))
    class Meta:
        model=Questions
        # fields={"exerciseDescription","exerciseTag"}
        fields={"questionDescription"}
