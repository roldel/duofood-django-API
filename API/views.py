from django.shortcuts import render

from .models import Ingredient, Recipe
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import IngredientSerializer, RecipeSerializer

#import UPDATE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Technical doc template renderer

def techdoc(request):
    return render(request, "API/techdoc.html")


#Endpoint 1 : Returns all Ingredient objects

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed.
    """
    queryset = Ingredient.objects.all()#.order_by('-date_joined')
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#Endpoint 2 : Return all Recipe objects

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#Endpoint 3

@api_view(['POST'])
def ingredientfilter(request):
    '''
    API endpoint that allows POST request with body key ["startswith"],
    it returns the ingredient objects filtered against the
    provided ["startswith"] key string value.
    '''
    if request.method == 'POST':
        begin = request.data['startswith']
        queryset = Ingredient.objects.filter(name__startswith=begin)
        serializer = IngredientSerializer(queryset, many=True)
        if len(queryset) == 0:
            return Response({'matching_ingredients': "no_match"})
        return Response({'matching_ingredients': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Endpoint 4

@api_view(['POST'])
def recipefilter(request):
    '''

    Answers POST request with Recipe objects filtered against ["ingredients"] JSON array must contain all
    '''
    avail_ingredient_list = request.data['ingredients']
    matching_recipe =[]
    for recipes in Recipe.objects.all():
        score = 0
        required_ingredients = recipes.ingredients.all()
        for i in required_ingredients:
            if str(i) in avail_ingredient_list:
                pass
            else:
                score += 1
        if score == 0:
            matching_recipe.append(recipes.id)
    queryset = Recipe.objects.filter(id__in = matching_recipe)
    if len(queryset) == 0:
            return Response({'matching_recipes': "no_match"})
    serializer = RecipeSerializer(queryset, many=True)
    return Response({'matching_recipes': serializer.data})