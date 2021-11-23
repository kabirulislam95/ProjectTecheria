from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from techeria_app.models import *


class Test_Product(TestCase):

    def test_fileds(self):

        def setUp(self):
             self.product = Products.object.create(
                name="HP Laptop, 17.3",
                price="899",
                description="128gb Silver",
                category="cell phone")

        def test_product_is_assigned_slug_on_creation(self):
            self.assertEqual(self.product.slug,'product')

class Test_laptop(TestCase):

    def test_fileds(self):

        def setUp(self):
             self.laptop = Laptops.object.create(
                name="HP Laptop, 17.3",
                price="899",
                description="11th Gen Intel Core i5-1135G7 Quad-Core Processor, 16GB DDR4 Memory",
                category="laptop")

        def test_laptop_is_assigned_slug_on_creation(self):
            self.assertEqual(self.laptop.slug,'laptop')


class Test_buyer(TestCase):
    def test_fileds(self):

        def setUp(self):
             self.buyer = BuyerModel.object.create(
                first_name = "Bruce",
                last_name = "Wayne",
                user_name = "batman",
                date_of_birth = "07/19/1995",
                email = "batman001@gmail.com",
                mobile_number ="7188888888",
                address = "1007 Mountain Drive",
                city = "Gotham",
                state = "NY",
                zip_code = "11512",
                country = "USA")

        def test_product_is_assigned_slug_on_creation(self):
            self.assertEqual(self.buyer.slug,'buyer')

class Test_seller(TestCase):
    def test_fileds(self):

        def setUp(self):
             self.seller = SellerModel.object.create(
                first_name = "Bruce",
                last_name = "Wayne",
                user_name = "batman",
                date_of_birth = "07/19/1995",
                email = "batman001@gmail.com",
                mobile_number ="7188888888",
                address = "1007 Mountain Drive",
                city = "Gotham",
                state = "NY",
                zip_code = "11512",
                country = "USA")

        def test_product_is_assigned_slug_on_creation(self):
            self.assertEqual(self.seller.slug,'seller')
