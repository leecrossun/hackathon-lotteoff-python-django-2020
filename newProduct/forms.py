from django import forms
from .models import NewProduct, Apply

class  ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('content', 'store_name', 'date_time',)