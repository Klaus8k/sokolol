from django.shortcuts import render

from .forms import OffsetForm

# Create your views here.


def offset_cost(request):
    print(request)
    if request.method == 'GET':
        form = OffsetForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)



    return render(request, template_name='order_cost_index.html', context={'form': form})









def order_cost(request):
    return offset_cost(request)
    
