from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'system', 'quantity', 'inv_num', 'placement', 'commissioning', 'depreciation']


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Оставьте комментарий'
        }
    ))
