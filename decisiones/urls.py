from django.urls import path
from .views import home, \
    FormularioListView, FormularioCreateView,  FormularioView, \
    GrupoListView, GrupoCreateView, GrupoUpdateView

urlpatterns = [
    path('', home, name='home'),
    # Grupos
    path('grupos/', GrupoListView.as_view(), name='grupo_list'),
    path('grupos/new', GrupoCreateView.as_view(), name='grupo_new'),
    path('grupos/edit/<int:pk>', GrupoUpdateView.as_view(), name='grupo_edit'),
    # Formularios
    path('formularios/', FormularioListView.as_view(), name='formulario_list'),
    path('formularios/new', FormularioCreateView.as_view(), name='formulario_new'),
    path('formularios/<int:pk>/', FormularioView.as_view(), name='formulario_view'),
]