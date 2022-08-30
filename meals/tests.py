from urllib import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Meal
from .forms import MealForm, IngredientForm

# Create your tests here.
class mealUrls(TestCase):
    def setUp(self):
        """
        Set up data to run the tests
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuserprofile", password="abc123def"
        )
        self.client.login(username="testuserprofile", password="abc123def")

    def test_meal_page_url(self):
        """
        test the meals page is accessible by name
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_ingredient_list_url(self):
        """
        test the ingredients page is accessible by name
        """
        response = self.client.get(reverse("shopping_list"))
        self.assertEqual(response.status_code, 200)


class mealForms(TestCase):
    def setUp(self):
        """
        Set up data to run the tests
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuserprofile", password="abc123def"
        )
        self.client.login(username="testuserprofile", password="abc123def")

    def test_ingredient_form(self):
        """
        test the  ingredient form is valid
        """
        data = {"name": "test ingredient"}
        form = IngredientForm(data)

        self.assertTrue(form.is_valid())

    def test_meal_add_form(self):
        """
        test the meal add form is valid
        """
        data = {
            "meal_name": "test meal",
            "meal_description": "test description",
        }
        form = MealForm(data)

        self.assertTrue(form.is_valid())



class testViewFunctions(TestCase):
    """
    test the view functions
    """

    def setUp(self):
        """
        Set up data to run the tests
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuserprofile", password="abc123def"
        )
        self.client.login(username="testuserprofile", password="abc123def")

    def test_meal_delete(self):
        """
        test the meal delete view works
        """
        meal = Meal.objects.create(
            meal_name="test meal",
            meal_description="test description",
            user=self.user,
        )
        response = self.client.post(
            reverse("deleted", kwargs={"meal_id": meal.id}), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Meal.objects.count(), 0)
