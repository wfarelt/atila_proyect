from django.urls import path
from .views import home, FormularioNew

urlpatterns = [
    path('', home, name='home'),
    path('formularios/new', FormularioNew.as_view(), name='formulario_new'),
]