from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    # title = forms.CharField(max_length=10)
    # content = forms.CharField()