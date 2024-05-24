from django.urls import path
from .views import home, FormularioNew, FormularioList, FormularioView

urlpatterns = [
    path('', home, name='home'),
    path('formularios/', FormularioList.as_view(), name='formulario_list'),
    path('formularios/new', FormularioNew.as_view(), name='formulario_new'),
    path('formularios/<int:pk>/', FormularioView.as_view(), name='formulario_view'),
]