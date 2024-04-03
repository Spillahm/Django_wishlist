from django import forms
from .models import place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = place
        fields = ('name', 'visited')
