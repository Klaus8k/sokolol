from django.shortcuts import render
from django.http import HttpResponseRedirect
from .logic import Json_obj, calc_solvent
from .parsers.parser import parce_m_grup

from my_logger import logger_view as logger

from .forms import OffsetForm, SolventForm, SolventSetForm

# Create your views here.
PAGES = ['offset', 'solvent', 'riso', 'stamp', 'oki']
pages_service = {'pages': PAGES, 'active': 'active', 'page_name': None}
PREFERENCE = 'order_cost/preference.json'


def view_decorator(view):
    """Decorator for view functions
    with pages param and cost settings"""
    def wrapp_context(request):
        cost_settings = Json_obj(PREFERENCE)
        context = {}
        context.update(pages_service)
        context['page_name'] = view.__name__
        context['cost'] = cost_settings.read()
        return view(request, context=context,   cost_settings=cost_settings)
    return wrapp_context


@view_decorator
def offset(request, context, cost_settings):
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = parce_m_grup(data)  # выполняестя расчет заказа
            context['form'] = form
        else:
            context['form'] = OffsetForm()
    return render(request, template_name='order_cost/offset.html', context=context)


@view_decorator
def solvent(request, context, cost_settings):

    if request.method == 'GET':
        form = SolventForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = calc_solvent(data, cost_settings)
            context['form'] = form
        else:
            context['form'] = SolventForm()

    if request.method == 'GET':
        form_set = SolventSetForm(request.GET)
        if form_set.is_valid():
            data = form_set.cleaned_data
            new_cost = {data['material']: data['price']}
            context['form_set'] = form_set
            cost_settings.write(new_cost, 'solvent')
    else:
        form_set = SolventSetForm()
    context['cost'] = cost_settings.read()
    return render(request, template_name='order_cost/solvent.html', context=context)


@view_decorator
def riso(request, context, cost_settings):
    return render(request, template_name='order_cost/riso.html', context=context)


@view_decorator
def stamp(request, context, cost_settings):
    return render(request, template_name='order_cost/stamp.html', context=context)


@view_decorator
def oki(request, context, cost_settings):

    return render(request, template_name='order_cost/oki.html', context=context)
