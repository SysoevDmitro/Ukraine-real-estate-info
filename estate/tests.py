from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import Address, Realtor, House, Owner
from django.urls import reverse


HOME_PAGE = reverse("estate:index")
REALTORS_LIST = reverse("estate:realtor-list")
HOUSE_LIST = reverse("estate:house-list")


class TestsForPublicRequired(TestCase):
    def test_login(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_realtor_list(self):
        response = self.client.get(REALTORS_LIST)
        self.assertEqual(response.status_code, 200)

    def test_house_list(self):
        response = self.client.get(HOUSE_LIST)
        self.assertEqual(response.status_code, 200)


class TestsForPrivateRequired(TestCase):
    def setUp(self) -> None:
        self.realtor = get_user_model().objects.create_user(
            username="test",
            password="dissom1987",
            rating=0.0
        )
        self.client.force_login(self.realtor)

    def test_login(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_realtor_list(self):
        response = self.client.get(REALTORS_LIST)
        self.assertEqual(response.status_code, 200)

    def test_house_list(self):
        response = self.client.get(HOUSE_LIST)
        self.assertEqual(response.status_code, 200)


class TestCreate(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin123"
        )
        self.client.force_login(self.admin_user)

        self.address = Address.objects.create(
            street='123 Main St',
            city='City',
            number=22,
            postal_code='12345'
        )
        self.realtor = Realtor.objects.create(
            rating=0.0
        )
        self.owner = Owner.objects.create(
            first_name='Owner',
            last_name='Owner',
            email='owner@example.com',
            phone_number='555234555'
        )
        self.house = House.objects.create(
            address=self.address,
            owner=self.owner,
            price=1000000,
            num_of_floors=2,
            num_of_bedrooms=2,
            area=200
        )
        self.house.realtor.set([self.realtor])

    def test_house_detail_view(self):
        response = self.client.get(f"/house/{self.house.id}/")
        self.assertEqual(response.status_code, 200)

    def test_realtor_detail_view(self):
        response = self.client.get("/realtor/1/")
        self.assertEqual(response.status_code, 200)

    def test_house_create_view(self):
        response = self.client.get("/houses/create/")
        self.assertEqual(response.status_code, 200)

    def test_realtor_create_view(self):
        response = self.client.get("/realtors/create/")
        self.assertEqual(response.status_code, 200)

