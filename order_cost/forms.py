from django import forms
from django.forms.widgets import NumberInput, RadioSelect

paper_weigh = [(130, 130), (170, 170), (300, 300)]
dublicate_choise = [(True,'4+4'),(False,'4+0')]
form_wiget = NumberInput(attrs={'class': 'offset_form'})


class OffsetForm(forms.Form):
    width = forms.IntegerField(required=None, min_value=0, max_value=1000,
                                label='Ширина', widget=form_wiget)
    higth = forms.IntegerField(required=None, min_value=0, max_value=1000,
                                label='Высота', widget=form_wiget)
    weigh = forms.ChoiceField(required=None,
                                label='Плотность', choices=paper_weigh)
    order = forms.IntegerField(required=None, min_value=0, max_value=100000,
                                label='Тираж', widget=form_wiget)
    dublicate = forms.BooleanField(required=None, widget=RadioSelect(choices=dublicate_choise))