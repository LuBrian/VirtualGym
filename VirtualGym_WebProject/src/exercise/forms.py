from django import forms
from .models import Exercise
"""/******************************
** File: forms.py
** Desc: This file interacts with the exercise model and given exercise forms in HTML
** Currently, Creating an Exercise is the only "form" that uses this in the exercise app.
*******************************/"""
# exercise tag choices for check box
TAG_CHOICE = (
    ('Shoulder', 'Shoulder'),
    ('Overhead', 'Overhead'),
    ('Elbow', 'Elbow'),
    ('Triceps', 'Triceps'),
    ('Biceps', 'Biceps'),
    ('Upright Rows', 'Upright Rows'),
    ('Diagonal_Inward_Shoulder', 'Diagonal_Inward_Shoulder'),
    ('Diagonal_Outward_Shoulder', 'Diagonal_Outward_Shoulder'),

)

class EditExeForm(forms.ModelForm):

    """
    exercise form for accept front end user input information for creating an exercise
    """

    # exercise descriptin input field
    exerciseDescription=forms.CharField(widget=forms.TextInput(
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
    exerciseTag=forms.CharField(required=False,widget=forms.TextInput(
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
    exerciseDescription=forms.CharField(widget=forms.TextInput(
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
    exTag=forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Tags for the exercise...",
           # "value":"test, test2",
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
