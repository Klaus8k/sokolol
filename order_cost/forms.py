from django import forms
from django.forms.widgets import NumberInput


class OffsetForm(forms.Form):
    width = forms.IntegerField(required=None, min_value=0, max_value=1000,
                               label='Ширина', widget=NumberInput(attrs={'class': 'offset_form'}))
    higth = forms.IntegerField(
        required=None, min_value=0, max_value=1000, label='Высота')
    weigh = forms.ChoiceField(required=None, label='Плотность', choices=[(130, 130),
                                                                             (170,
                                                                              170),
                                                                             (300, 300)])
    order = forms.IntegerField(
        required=None, min_value=0, max_value=100000, label='Тираж')
