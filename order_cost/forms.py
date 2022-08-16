from django import forms
from django.forms.widgets import NumberInput

class OffsetForm(forms.Form):
    width = forms.IntegerField(required=None, min_value=0 , max_value=1000, label='Ширина', widget=NumberInput(attrs={'class': 'offset_form'}))
    higth = forms.IntegerField(required=None,min_value=0 , max_value=1000, label='Высота')
    # 4+4 4+0 required=None,
    order = forms.IntegerField(required=None,min_value=0 , max_value=100000, label='Тираж')
