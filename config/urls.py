from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from API import views


router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'recipe', views.RecipeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    #Technical documentation manual ruoting
    path('techdoc', views.techdoc),

    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Endpoint 3
    path('ingredientfilter', views.ingredientfilter),

    #Endpoint 4
    path('recipefilter', views.recipefilter),
]