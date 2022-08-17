from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OffsetForm, SolventForm

# Create your views here.


def offset_cost(request):
    pass


def result(data: dict):
    return data


def order_cost(request):
    print('-----', request, '-----')
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context = data
            context['result'] = result(data)
            context['form'] = form
            print(context)
    else:
        context = {}
        context['form'] = OffsetForm()
    return render(request, template_name='order_cost_index.html', context=context)
