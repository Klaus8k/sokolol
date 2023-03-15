
from django.urls import path
from django.views.generic.base import TemplateView

from .views import Dev_view


app_name = 'dev'
urlpatterns = [
    path('', Dev_view.as_view(), name='dev'),
]