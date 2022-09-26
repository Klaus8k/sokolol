from django.shortcuts import render
from django.http import HttpResponseRedirect
from .logic import Json_obj, calc_solvent

from .forms import OffsetForm, SolventForm, SolventSetForm

# Create your views here.
pages = ['offset', 'solvent', 'riso', 'stamp', 'oki']
pages_service = {'pages': pages, 'active': 'active', 'page_name': None}
preference = 'order_cost/preference.json'


# decorator for send page info
def view_decorator(view):
    def wrapp_context(request):
        context = {}
        context.update(pages_service)
        context['page_name'] = view.__name__
        return view(request, context=context)
    return wrapp_context

@view_decorator
def offset(request, context):
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = data  # выполняестя расчет заказа
            context['form'] = form
            print(context)
        else:
            context['form'] = OffsetForm()
    # context.update(pages_serv)
    # context['page_name'] = 'offset'
    return render(request, template_name='order_cost/offset.html', context=context)


# Block for reset price and stuff price
@view_decorator
def solvent(request, context):
    cost = Json_obj(preference)
    # context.update(pages_serv)
    # context['page_name'] = 'solvent'

    if request.method == 'GET':
        form = SolventForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = calc_solvent(data, cost)
            context['form'] = form
        else:
            context['form'] = SolventForm()

    if request.method == 'GET':
        form_set = SolventSetForm(request.GET)
        if form_set.is_valid():
            data = form_set.cleaned_data
            new_cost = {data['material']: data['price']}
            context['form_set'] = form_set
            cost.write(new_cost, 'solvent')
    else:
        form_set = SolventSetForm()
    context['cost'] = cost.read()
    return render(request, template_name='order_cost/solvent.html', context=context)


def oki(request):
    context = {}
    context.update(pages_serv)
    context['page_name'] = 'oki'

    return render(request, template_name='order_cost/oki.html', context=context)
