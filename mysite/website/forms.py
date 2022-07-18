from django import forms
from website.models import connect
from website.models import comment

class connectform(forms.ModelForm):
    class Meta:
        model=connect
        fields="__all__"

class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields="__all__"