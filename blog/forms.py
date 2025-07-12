from django import forms
from .models import Publication,Commentaire

class PubForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('auteur',)