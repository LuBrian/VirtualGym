from django import forms
from .models import Question

class QuestionsForm(forms.ModelForm):

    """
    question form for accept front end user input information
    """
    # question descriptin input field
    questionDescription = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Your Answer...",
        }
    ))
    class Meta:

        """
        question comment fields in front end
        """
        model=Question
        fields={"questionDescription"}
