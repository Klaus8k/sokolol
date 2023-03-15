from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse

# Create your views here.
class Dev_view(View):

    def get(sefl, *args, **kwargs):
        return HttpResponse('<h1>Sub Domen dev.####.ru</h1>')
