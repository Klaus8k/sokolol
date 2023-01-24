from django import forms
from django.forms import widgets

form_wiget = 0

material_choise = [('banner', 'Баннер'), ('sticker', 'Наклейка'), ('tabl', 'Табличка')]

class SolventForm(forms.Form):
    type_order = forms.CharField(initial='solvent', label='Сольвентная печать',
                                 widget=widgets.TextInput(attrs={'style': 'display: none'}))
    width = forms.FloatField(required=None, min_value=0, max_value=100,
                               label='Ширина (м)', widget=form_wiget)
    higth = forms.FloatField(required=None, min_value=0, max_value=100,
                               label='Высота (м)', widget=form_wiget)
    material = forms.ChoiceField(required=None,
                              label='Материал', choices=material_choise)
