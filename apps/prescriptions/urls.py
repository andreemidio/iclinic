from django.urls import path, include
from rest_framework import routers

from apps.produtos.viewsets import PostProdutosViewSets, DestroyProdutosViewSets, UpdateProdutosViewSets, \
    RetriveProdutosViewSets, ListProdutosViewSets

app_name = 'produtos'

router = routers.DefaultRouter()
router.register(r'cadastrar-produtos', PostProdutosViewSets, basename='cadastrar-produtos')
router.register(r'listar-produtos', ListProdutosViewSets, basename='listar-produtos')
router.register(r'detalhes-produto', RetriveProdutosViewSets, basename='detalhes-produto')
router.register(r'atualizar-produto', UpdateProdutosViewSets, basename='atualizar-produto')
router.register(r'deletar-produto', DestroyProdutosViewSets, basename='deletar-produto')

urlpatterns = [
    path(r'', include(router.urls)),
]
