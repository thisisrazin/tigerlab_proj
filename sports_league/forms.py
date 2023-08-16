from django import forms
from .models import MatchResult_File, Match

class UploadForm(forms.ModelForm):
    class Meta:
        model=MatchResult_File
        fields=('resultID', 'documentCSV',)

        widgets={
            'resultID': forms.HiddenInput(),
            'documentCSV': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class AddMatchForm(forms.ModelForm):
    class Meta:
        model=Match
        fields=('resultFile', 'teamOne', 'teamTwo', 'teamOneScore', 'teamTwoScore')

        widgets={
            'resultFile': forms.HiddenInput(),
            'teamOne': forms.TextInput(attrs={'class': 'form-control'}),
            'teamTwo': forms.TextInput(attrs={'class': 'form-control'}),
            'teamOneScore': forms.TextInput(attrs={'class': 'form-control'}),
            'teamTwoScore': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateMatchForm(forms.ModelForm):
    class Meta:
        model=Match
        fields=('resultFile', 'teamOne', 'teamTwo', 'teamOneScore', 'teamTwoScore')

        widgets={
            'resultFile': forms.HiddenInput(),
            'teamOne': forms.TextInput(attrs={'class': 'form-control'}),
            'teamTwo': forms.TextInput(attrs={'class': 'form-control'}),
            'teamOneScore': forms.TextInput(attrs={'class': 'form-control'}),
            'teamTwoScore': forms.TextInput(attrs={'class': 'form-control'}),
        }

