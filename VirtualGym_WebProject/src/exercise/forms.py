from django import forms
from .models import Exercise

class CreateExeForm(forms.ModelForm):
    exerciseDescription=forms.CharField()
    exTag = forms.CharField(label='''Exercise Tags separated by ","''', max_length = 500)
    topVideo=forms.FileField(label="Top Video Perspective", required=False)
    backVideo=forms.FileField(label="Back Video Perspective", required=False)
    frontVideo=forms.FileField(label="Front Video Perspective", required=False)
    leftVideo=forms.FileField(label="Left Video Perspective", required=False)
    rightVideo=forms.FileField(label="Right Video Perspective", required=False)
    threeQuartersVideo = forms.FileField(label="Three Quarters Video Perspective", required=False)
    # exercisePosterId=forms.CharField()
    class Meta:
        model=Exercise
        # fields={"exerciseDescription","exerciseTag"}
        fields={"exerciseDescription"}
