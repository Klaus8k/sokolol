from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin
from django.views.generic.list import MultipleObjectMixin

from my_logger import logger_view as logger
import loguru

from .forms import (OffsetForm, RisoForm, RisoSetForm, SolventForm, material_choise,
                    SolventSetForm)
from .logic import check_db_or_calc_and_save, riso_calc, save_to_db
from .models import Offset_model, Riso_model, Solvent_model

# Create your views here.
PAGES = ['offset', 'solvent', 'riso']
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
            context['result'] = check_db_or_calc_and_save(
                data)  # выполняестя расчет заказа
            context['form'] = form
        else:
            context['form'] = OffsetForm()
    return render(request, template_name='order_cost/offset.html', context=context)


@view_decorator
def solvent(request, context):


    if request.method == 'GET':
        context['form'] = SolventForm()
        context['form_set'] = SolventSetForm()

    elif request.method == 'POST':
        
        current_cost_solvent = []

        if Solvent_model.objects.exists():
            mat_choise_clean = [i[0] for i in material_choise]
            for field in mat_choise_clean:
                current_cost_solvent.append(Solvent_model.objects.filter(type_prod=field).latest('date'))
            context['solvent_db'] = current_cost_solvent
        else:
            context['result'] = 'Для расчета нет данных о расходниках'
            
        if 'cost' in request.POST.keys():
            context['form'] = SolventForm()
            form_set = SolventSetForm(request.POST)
            if form_set.is_valid():
                data = form_set.cleaned_data
                new_cost = save_to_db(data)
                context['form_set'] = form_set
                context['cost'] = new_cost

        else:
            context['form_set'] = SolventSetForm()
            form = SolventForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                context.update(data)
                context['result'] = check_db_or_calc_and_save(data)
                context['form'] = form

    return render(request, template_name='order_cost/solvent.html', context=context)


# Вьюха на основе класса
class Riso_view(View, ContextMixin):
    """"""
    form_class = RisoForm
    set_form_class = RisoSetForm
    initial = {'key': 'value'}
    template_name = 'order_cost/riso.html'
    model = Riso_model
    ordering = '-date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(initial=self.initial)
        form_set = self.set_form_class(initial=self.initial)
        context = {'form': form, 'form_set': form_set}
        context.update(pages_service)
        context['page_name'] = 'riso'
        context['riso_db'] = Riso_model.objects.latest('date')
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, *args, **kwargs):
        
        data = self.request.POST.dict()
        
        if 'paper_cost_80' in request.POST.keys():
                riso_calc(data)
                context = self.get_context_data()
                

        else:
            if len(Riso_model.objects.all()) > 0:
                context = self.get_context_data()
                context.update({'result': riso_calc(data)})
            else:
                result='В базе данных нет информации о расходника'

        return render(request, self.template_name, context=context)

