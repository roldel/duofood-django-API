from .models import Ingredient, Recipe
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)
    class Meta:
        model = Recipe
        fields = ['id','name', 'text', 'picture','ingredients']