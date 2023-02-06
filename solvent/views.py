from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from . import forms

# Create your views here.

class Solvent_view(FormView):
    form_class = forms.SolventForm
    template_name = 'solvent_app.html'
    
    def form_valid(self, form: object) -> HttpResponse:
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        print(request)
        context = {}
        context['result'] = 1000
        return render(request=self.request, template_name=self.template_name, *args, **kwargs, context=context)
    