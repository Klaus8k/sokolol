from django.shortcuts import render
from django.http import HttpResponseRedirect
from .logic import Json_obj, calc_solvent, solvent_check_and_save_or_return, save_to_db
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
        # cost_settings = Json_obj(PREFERENCE)
        context = {}
        context.update(pages_service)
        context['page_name'] = view.__name__
        # context['cost'] = cost_settings.read()
        return view(request, context=context)
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
def solvent(request, context):

    context['form'] = SolventForm()
    context['form_set'] = SolventSetForm()

    if request.method == 'POST':
        form = SolventForm(request.POST)
        form_set = SolventSetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = solvent_check_and_save_or_return(data)
            context['form'] = form
        elif form_set.is_valid():
            data = form_set.cleaned_data
            new_cost = save_to_db(data)
            context['form_set'] = form_set
            context['cost'] = new_cost
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
