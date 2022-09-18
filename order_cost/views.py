from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OffsetForm, SolventForm, SolventSetForm

# Create your views here.
pages = [ 'offset', 'solvent', 'riso', 'stamp', 'oki']

# decorator for send page info

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
    context['pages'] = pages
    context['active'] = 'active'
    context['page_name']  = 'offset'
    return render(request, template_name='order_cost/offset.html', context=context)


# Block for reset price and stuff price
def solvent(request):
    if request.method == 'GET':
        form = SolventForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context = data
            context['result'] = data
            context['form'] = form
            print(context)
        else:
            context = {}
            context['form'] = SolventForm()
    context['pages'] = pages
    context['active'] = 'active'
    context['page_name']  = 'solvent'


    form_set = SolventSetForm()
    context['form_set'] = form_set
    return render(request, template_name='order_cost/solvent.html', context=context)


def oki(request):
    context = {}
    context['pages'] = pages
    context['active'] = 'active'
    context['page_name']  = 'oki'

    return render(request, template_name='order_cost/oki.html', context=context)