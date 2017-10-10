from apps.beer.models import Beer
from django import forms


class BeerForm(forms.ModelForm):
    class Meta:
        model=Beer
        exclude=[]