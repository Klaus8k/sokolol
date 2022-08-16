from django import forms

class OffsetForm(forms.Form):
    width = forms.IntegerField(min_value=0 , max_value=1000)
    higth = forms.IntegerField(min_value=0 , max_value=1000)
    # 4+4 4+0 
    order = forms.IntegerField(min_value=0 , max_value=1000000)
