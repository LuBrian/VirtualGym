from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"your comments...",
        }
    ))
    #parent_id=forms.IntegerField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Comment
        # fields={"exerciseDescription","exerciseTag"}
        fields={"content"}
