from django.http import HttpResponseRedirect
from django.shortcuts import render

from my_logger import logger_view as logger

from .forms import OffsetForm, SolventForm, SolventSetForm
from .logic import check_db_or_calc_and_save, save_to_db
from .models import Solvent_model, Offset_model

# Create your views here.
PAGES = ['offset', 'solvent', 'riso', 'stamp', 'oki']
pages_service = {'pages': PAGES, 'active': 'active', 'page_name': None}


def view_decorator(view):
    """Decorator for view functions
    with pages param for nav-menu"""
    def wrapp_context(request):
        context = {}
        context.update(pages_service)
        context['page_name'] = view.__name__
        return view(request, context=context)
    return wrapp_context


@view_decorator
def offset(request, context):
    context['offset_db'] = Offset_model.objects.all()

    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = check_db_or_calc_and_save(data)  # выполняестя расчет заказа
            context['form'] = form
        else:
            context['form'] = OffsetForm()
    return render(request, template_name='order_cost/offset.html', context=context)


@view_decorator
def solvent(request, context):
    context['solvent_db'] = Solvent_model.objects.all()
    context['form'] = SolventForm()
    context['form_set'] = SolventSetForm()

    if request.method == 'POST':
        form = SolventForm(request.POST)
        form_set = SolventSetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context.update(data)
            context['result'] = check_db_or_calc_and_save(data)
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
