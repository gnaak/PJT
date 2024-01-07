from django import forms
from .models import Keyword, Trend

class KeywordForm(forms.ModelForm):
    name = forms.CharField(label="Keyword")
    class Meta:
        model = Keyword
        fields = '__all__'
        


class TrendForm(forms.ModelForm):
    class Meta:
        model = Trend
        fields = '__all__'
        