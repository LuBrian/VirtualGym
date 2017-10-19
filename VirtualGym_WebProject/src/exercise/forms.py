from django import forms
from .models import Exercise

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


    exerciseDescription=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Description for your exercise...",
        }
    ))
 
    exerciseTag = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICE,
    )
    exTag = forms.CharField(label='''Exercise Tags separated by ","''', max_length = 500, required=False)
    exerciseVideos=forms.FileField()
    # exercisePosterId=forms.CharField()
    class Meta:
        model=Exercise
        # fields={"exerciseDescription","exerciseTag"}
        fields={"exerciseDescription","exerciseTag","exerciseVideos","exercisePosterId"}
