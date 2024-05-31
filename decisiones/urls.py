from django.urls import path
from .views import home, \
    FormularioListView, FormularioCreateView, balance_general

urlpatterns = [
    path('', home, name='home'),
    # Formularios
    path('formularios/', FormularioListView.as_view(), name='formulario_list'),
    path('formularios/new', FormularioCreateView.as_view(), name='formulario_new'),
    # Balance General
    path('balance_general/', balance_general, name='balance_general'),
]