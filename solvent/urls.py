from django.urls import path
from .views import Solvent_view

urlpatterns = [
    path('', Solvent_view.as_view())

]