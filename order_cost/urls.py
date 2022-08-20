from unicodedata import name
from django.views.generic.base import TemplateView
from django.urls import path
from .views import offset, solvent
from order_cost import views


app_name = 'order_cost'
urlpatterns = [
    path('', TemplateView.as_view(template_name='order_cost_index.html')),
    path('offset/', views.offset, name='offset'),
    path('solvent/', views.solvent, name='solvent'),
    path('oki/', views.oki, name='oki'),



]
# Add path's for other page in app order_cost
