from django import forms
from .models import Exercise
"""/******************************
** File: forms.py
** Desc: This file interacts with the exercise model and given exercise forms in HTML
** Currently, Creating an Exercise is the only "form" that uses this in the exercise app.
*******************************/"""
# exercise tag choices for check box
TAG_CHOICE = (
    ('Biceps', 'Biceps'),
    ('Diagonal Inward Shoulder', 'Diagonal Inward Shoulder'),
    ('Diagonal Outward Shoulder', 'Diagonal Outward Shoulder'),
    ('Elbow', 'Elbow'),
    ('Overhead', 'Overhead'),
    ('Shoulder', 'Shoulder'),
    ('Triceps', 'Triceps'),
    ('Upright Rows', 'Upright Rows'),
)

class EditExeForm(forms.ModelForm):

    """
    exercise form for accept front end user input information for creating an exercise
    """

    # exercise descriptin input field
    exerciseDescription=forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Description for your exercise...",
        }
    ))

    exerciseName=forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"Title for your exercise...",
        }
    ))

    # exercise tag text input field
    exerciseTag=forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Tags for the exercise...",
        }
    ))

    # exercise video input field
    exerciseVideos=forms.FileField()

    class Meta:

        """
        set exercise fields in front end
        """
        model=Exercise
        fields={"exerciseDescription","exerciseTag","exerciseVideos","exerciseName"}


class CreateExeForm(forms.ModelForm):

    """
    exercise form for accept front end user input information for creating an exercise
    """

    # exercise descriptin input field
    exerciseDescription=forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Description for your exercise...",
        }
    ))

    exerciseName=forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"Title for your exercise...",
        }
    ))

    # exercise tag input check box field
    exerciseTag = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICE,
    )

    # exercise tag text input field
    exTag=forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Tags for the exercise...",
           # "value":"test, test2",
        }
    ))


    # exercise video input field
    exerciseVideos1=forms.FileField()
    exerciseVideos2=forms.FileField(required=False)
    exerciseVideos3=forms.FileField(required=False)
    exerciseVideos4=forms.FileField(required=False)
    exerciseVideos5=forms.FileField(required=False)
    class Meta:

        """
        set exercise fields in front end
        """
        model=Exercise
        fields={"exerciseDescription","exerciseTag","exerciseName"}
