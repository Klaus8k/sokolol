from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OffsetForm

# Create your views here.


def offset_cost(request):

    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            context = data
            context['result'] = result(data)
            context['form'] = form
            print(context)
    else:
        context['form'] = OffsetForm()

    return render(request, template_name='order_cost_index.html', context=context)


def result(data: dict):
    print(data)
    result = 0
    for i in data.values():
        print(i, result)
        if isinstance(i, int):
            result += i
    
    return result


def order_cost(request):
    return offset_cost(request)
