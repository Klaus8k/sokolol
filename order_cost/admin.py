from django.contrib import admin

from .models import Offset_model, Solvent_model

# Register your models here.

admin.site.register(Solvent_model)
admin.site.register(Offset_model)
