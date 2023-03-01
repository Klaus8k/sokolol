from django.contrib import admin

from .models import Offset_model, Solvent_model, Type_Order, Riso_model

# Register your models here.

registred_models = [Solvent_model, Offset_model, Type_Order, Riso_model]

admin.site.register(registred_models)
