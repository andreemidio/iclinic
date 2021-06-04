from rest_framework import serializers

from apps.categorias.serializers import ListCategoriaProdutosSerializers, PostCategoriaProdutosSerializers
from apps.produtos.models import Produtos
from apps.usuarios.serializers import GetUsuariosSerializers


class PostProdutosSerializers(serializers.ModelSerializer):
    criado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # categorias = PostCategoriaProdutosSerializers(many=True)

    class Meta:
        model = Produtos
        # fields = ('id', 'nome', 'descricao' 'preco', 'criado_por')
        fields = '__all__'


class ListProdutosSerializers(serializers.ModelSerializer):
    categorias = ListCategoriaProdutosSerializers(many=True)

    class Meta:
        model = Produtos
        fields = ('id', 'nome', 'descricao', 'preco', 'categorias')


class RetriveProdutosSerializers(serializers.ModelSerializer):
    categorias = ListCategoriaProdutosSerializers(many=True)
    criado_por = GetUsuariosSerializers()

    class Meta:
        model = Produtos
        fields = ('id', 'nome', 'descricao', 'preco', 'categorias', 'criado_por')


class UpdateProdutosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('id', 'nome', 'descricao', 'preco', 'categorias')
