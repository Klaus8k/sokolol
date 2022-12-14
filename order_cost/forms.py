from django import forms
from django.forms import widgets

paper_weigh = [(130, 130), (170, 170), (300, 300)]
duplex_choise = [(True, '4+4'), (False, '4+0')]
form_wiget = widgets.NumberInput(attrs={'class': 'offset_form'}) # class html for css preference 'offset_form'


class OffsetForm(forms.Form):
    type_order = forms.CharField(initial='offset', label='Офсетная печать',
                                 widget=widgets.TextInput(attrs={'style': 'display: none'}))
    formatX = forms.IntegerField(required=None, min_value=0, max_value=1000,
                               label='Ширина (мм)', widget=form_wiget)
    formatY = forms.IntegerField(required=None, min_value=0, max_value=1000,
                               label='Высота (мм)', widget=form_wiget)
    density = forms.ChoiceField(required=None,
                              label='Плотность (г/м)', choices=paper_weigh)
    pressrun = forms.IntegerField(required=None, min_value=0, max_value=100000,
                               label='Тираж (шт)', widget=form_wiget)
    duplex = forms.BooleanField(required=None, label='4+4/4+0',
                                   widget=widgets.RadioSelect(choices=duplex_choise))

    


material_choise = [('banner', 'Баннер'), ('sticker', 'Наклейка'), ('tabl', 'Табличка')]

class SolventForm(forms.Form):
    type_order = forms.CharField(initial='solvent', label='Широкоформатная печать',
                                 widget=widgets.TextInput(attrs={'style': 'display: none'}))
    width = forms.FloatField(required=None, min_value=0, max_value=100,
                               label='Ширина (м)', widget=form_wiget)
    higth = forms.FloatField(required=None, min_value=0, max_value=100,
                               label='Высота (м)', widget=form_wiget)
    material = forms.ChoiceField(required=None,
                              label='Материал', choices=material_choise)


class SolventSetForm(forms.Form):

    material = forms.ChoiceField(required=None,
                                label='Материал (квм)', choices=material_choise)
    price = forms.IntegerField(required=None, label='Цена закупки')
