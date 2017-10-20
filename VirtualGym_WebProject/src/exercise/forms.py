from django import forms
from .models import Exercise

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

class CreateExeForm(forms.ModelForm):

    """
    exercise form for accept front end user input information
    """

    # exercise descriptin input field
    exerciseDescription=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Description for your exercise...",
        }
    ))

    # exercise tag input check box field
    exerciseTag = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICE,
    )

    # exercise tag text input field
    exTag = forms.CharField(label='''Exercise Tags separated by ","''', max_length = 500, required=False)

    # exercise video input field
    exerciseVideos=forms.FileField()

    class Meta:

        """
        set exercise fields in front end
        """
        model=Exercise
        fields={"exerciseDescription","exerciseTag","exerciseVideos"}
