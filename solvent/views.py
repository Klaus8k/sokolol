from django.shortcuts import render
from django.views.generic.edit import FormView
from . import forms
# Create your views here.

class Solvent_view(FormView):
    form_class = forms.SolventForm
    template_name = 'solvent.html'
