from django import forms
from .models import *

class AddUrlForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Ссылка')

class HistoryForm(forms.Form):
    class Meta():
        model = History
        fields = '__all__'


    
