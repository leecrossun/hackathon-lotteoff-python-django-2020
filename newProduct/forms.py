from django import forms
from .models import NewProduct, Apply, Evaluation

class  ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('content', 'store_name', 'date_time',)

class Evaluation(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ('e_title', 'e_content')