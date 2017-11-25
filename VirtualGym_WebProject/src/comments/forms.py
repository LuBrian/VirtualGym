from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    """
    comment form for accept front end user input information
    """

    # comment descriptin input field
    comment=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Type your comment here...",
        }
    ))

    class Meta:
        """
        set comment fields in front end
        """
        model=Comment
        fields={"comment"}
