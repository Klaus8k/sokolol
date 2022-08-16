from django.views.generic.base import TemplateView
from django.urls import path
from .views import order_cost


app_name = 'order_cost'
urlpatterns = [
    path('', order_cost, name='order_cost'),
]
