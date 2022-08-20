from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OffsetForm, SolventForm

# Create your views here.
pages = ['main', 'offset', 'solvent', 'riso', 'stamp', 'oki']

def offset(request):
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context = data
            context['result'] = data
            context['form'] = form
            print(context)
        else:
            context = {}
            context['form'] = OffsetForm()
    return render(request, template_name='order_cost/offset.html', context=context)

def solvent(request):
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context = data
            context['result'] = data
            context['form'] = form
            print(context)
        else:
            context = {}
            context['form'] = OffsetForm()
    context['pages'] = pages
    context['active'] = 'active'
    context['page_name']  = 'solvent'
    return render(request, template_name='order_cost/solvent.html', context=context)


def oki(request):
    context = {}
    context['pages'] = pages
    context['active'] = 'active'
    context['page_name']  = 'oki'
    return render(request, template_name='order_cost/oki.html', context=context)