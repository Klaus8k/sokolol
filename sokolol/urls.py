
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView  # класс для вызова шаблона
from django.conf.urls.static import static
from . import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index_sokolol.html')),
    path('order_cost/', include('order_cost.urls')),
    path('tipkor/', TemplateView.as_view(template_name='tipkor.html')),
    path('timer/', TemplateView.as_view(template_name='timer.html'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
