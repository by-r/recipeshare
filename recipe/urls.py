from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeListView.as_view(), name="RecipeList"),
    path("create/", views.RecipeCreateView.as_view(), name="RecipeCreate"),
    path("update/<int:pk>", views.RecipeUpdateView.as_view(), name="RecipeUpdate"),
    path("delete/<int:pk>", views.RecipeDeleteView.as_view(), name="RecipeDelete"),
]
