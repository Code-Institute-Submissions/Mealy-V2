from . import views
from django.urls import path

urlpatterns = [
    path("", views.MealList.as_view(), name="home"),
    path("list", views.ShopList.as_view(), name="shopping_list"),
    path("toggle_planned/<meal_id>", views.toggle_planned, name="toggle"),
    path("delete_meal/<meal_id>", views.delete_meal, name="deleted"),
    path("add", views.add_ingredient, name="add"),]