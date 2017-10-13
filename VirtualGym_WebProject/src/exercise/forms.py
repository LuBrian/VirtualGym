from django import forms
from .models import Exercise

TAG_CHOICE = (
    ('Shoulder', 'Shoulder'),
    ('Overhead', 'Overhead'),
    ('Elbow', 'Elbow'),
    ('Triceps', 'Triceps'),
    ('Biceps', 'Biceps'),
    ('Upright Rows', 'Upright Rows'),
    ('Diagonal Inward Shoulder', 'Diagonal Inward Shoulder'),
    ('Diagonal Outward Shoulder', 'Diagonal Outward Shoulder'),

)

class CreateExeForm(forms.ModelForm):


    exerciseDescription=forms.CharField()
    exerciseTag = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICE,
    )
    exerciseVideos=forms.FileField()
    # exercisePosterId=forms.CharField()
    class Meta:
        model=Exercise
        # fields={"exerciseDescription","exerciseTag"}
        fields={"exerciseDescription","exerciseTag","exerciseVideos"}
