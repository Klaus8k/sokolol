
from django.urls import path
from django.views.generic.base import TemplateView

from order_cost import views

from .views import Riso_view, offset, solvent

app_name = 'order_cost'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='order_cost_index.html')),
    path('offset/', views.offset, name='offset'),
    path('solvent/', views.solvent, name='solvent'),
    path('riso/', Riso_view.as_view(), name='riso'), 
    ]
# Add path's for other page in app order_cost
