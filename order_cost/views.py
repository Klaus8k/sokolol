from django.shortcuts import render

from .forms import OffsetForm

# Create your views here.


def offset(request):
    context = {'current_name': '1111111111'}
    form = OffsetForm()
    context['form'] = form
    return render(request=request, template_name='order_cost_index.html', context=context)


def order_cost(request):

    print(request)
    return offset(request)
    
