from django.test import TestCase
# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from techeria_app.models import *
from techeria_app.models import Products, Laptops, Smartphone


class Test_Product(TestCase):

    def test_fileds(self):
        def setUp(self):
            self.product = Products.object.create(
                name="iPhone13pro",
                price="999",
                description="128gb Silver",
                category="smartphone")

        def test_product_model(self):
            d = self.techeria_app
            self.assertTrue(isinstance(d, Products))
            self.assertEqual(str(d), ' iPhone13pro')


class Test_laptop(TestCase):

    def test_fileds(self):

        def setUp(self):
            self.laptop = Laptops.object.create(
                name=" HP Laptop, 17.3",
                price=" 899",
                description=" 11th Gen Intel Core i5-1135G7 Quad-Core Processor, 16GB DDR4 Memory",
                category=" laptop")

        def test_laptop_is_assigned_slug_on_creation(self):
            self.assertEqual(self.laptop.slug, ' laptop')


class Test_smartphone(TestCase):

    def test_fileds(self):
        def setUp(self):
            self.smartphone = Smartphone.object.create(
                name=" Samsung - Galaxy S21",
                price=" 1299.99",
                description=" Galaxy S21 Ultra 5G for verizon is crafted",
                category=" smartphone")

        def test_smartphone_is_assigned_slug_on_creation(self):
            self.assertEqual(self.smartphone.slug, ' smartphone')
