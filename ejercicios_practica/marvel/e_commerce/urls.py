from django.urls import path, include
from e_commerce.api.api_views import PostComicAPIView

from .views import *


urlpatterns = [
    path('tabla/',TableView.as_view(),name='tabla'),
    path('lista/',ListaView.as_view(), name='lista'),
    path('formulario/',FormularioView.as_view()),
    path('imagen/',ImagenView.as_view(),name='imagen'),
    path('agregar-comic/',AgregarComicView.as_view()),
    	]