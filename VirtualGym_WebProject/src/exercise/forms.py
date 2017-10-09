from django import forms
from .models import Exercise

class CreateExeForm(forms.ModelForm):
    exerciseDescription=forms.CharField()
    exerciseTag=forms.CharField()
    exerciseVideos=forms.FileField()
    # exercisePosterId=forms.CharField()
    class Meta:
        model=Exercise
        # fields={"exerciseDescription","exerciseTag"}
        fields={"exerciseDescription","exerciseTag","exerciseVideos"}
