from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = [
            'title',
            'description'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise forms.ValidationError("A wish must consist of at least 3 characters!")
        return title 

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get("description")
        if len(description) < 1:
            raise forms.ValidationError("A description must be provided!")
        if len(description) < 3:
            raise forms.ValidationError("A wish description must consist of at least 3 characters!")
        return description 
            