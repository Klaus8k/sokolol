from django import forms
from django.forms import widgets

paper_weigh = [(130, 130), (170, 170), (300, 300)]
duplex_choise = [(True, '4+4'), (False, '4+0')]
riso_formats = [('A4', 'A4',), ('A5', 'A5',), ('A6', 'A6',)]
# class html for css preference 'offset_form'
form_wiget = widgets.NumberInput(attrs={'class': 'offset_form'})


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


material_choise = [('banner', 'Баннер'),
                   ('sticker', 'Наклейка'),
                   ('tabl', 'Табличка')]


class SolventForm(forms.Form):
    type_order = forms.CharField(initial='solvent', label='Широкоформатная печать',
                                 widget=widgets.TextInput(attrs={'style': 'display: none'}))
    width = forms.FloatField(required=True, min_value=0, max_value=100,
                             label='Ширина (м)', widget=form_wiget)
    higth = forms.FloatField(required=True, min_value=0, max_value=100,
                             label='Высота (м)', widget=form_wiget)
    type = forms.ChoiceField(required=True,
                             label='Материал', choices=material_choise)


class SolventSetForm(forms.Form):
    type_order = forms.CharField(initial='solvent', label='Широкоформатная печать',
                                 widget=widgets.TextInput(attrs={'style': 'display: none'}))
    type = forms.ChoiceField(required=True,
                             label='Материал (квм)', choices=material_choise)
    cost = forms.IntegerField(required=True, label='Цена закупки')


class RisoForm(forms.Form):
    format = forms.ChoiceField(
        required=True, label='Формат:', choices=riso_formats)
    pressrun = forms.IntegerField(min_value=200, label='Тираж', required=True)


class RisoSetForm(forms.Form):
    paper_cost_80 = forms.IntegerField(required=True,
        label='Цена за пачку 500л')
    black_ink_cost = forms.IntegerField(required=True,
        label='Цена за банку краски')
    master_list_cost = forms.IntegerField(required=True,
        label='Цена мастер пленки')
