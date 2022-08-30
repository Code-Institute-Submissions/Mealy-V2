from .models import Meal, Ingredient
from django import forms

class IngredientForm(forms.ModelForm):
    """Ingredients Form"""
    class Meta:
        model = Ingredient
        widgets = {"name": forms.widgets.TextInput}
        fields = ("name",)


class MealForm(forms.ModelForm):
    """Meal form"""
    class Meta:
        model = Meal
        widgets = {'ingredients': forms.widgets.CheckboxSelectMultiple() }
        fields = ("meal_name", "meal_description", "planned", "ingredients",)


