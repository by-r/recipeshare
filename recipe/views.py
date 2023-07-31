from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Recipe

# Create your views here.

class RecipeBaseView(View):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('RecipeList')

class RecipeListView(RecipeBaseView, ListView):
    context_object_name = 'recipe_list'

class RecipeCreateView(RecipeBaseView, CreateView):
    """_summary_

    Args:
        RecipeBaseView (_type_): _description_
        CreateView (_type_): _description_
    """

class RecipeUpdateView(RecipeBaseView, UpdateView):
    """_summary_

    Args:
        RecipeBaseView (_type_): _description_
        UpdateView (_type_): _description_
    """

class RecipeDeleteView(RecipeBaseView, DeleteView):
    """_summary_

    Args:
        RecipeBaseView (_type_): _description_
        DeleteView (_type_): _description_
    """
