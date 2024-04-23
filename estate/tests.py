from django.test import TestCase
from django.contrib.auth import get_user_model


from django.urls import reverse


HOME_PAGE = reverse("estate:index")
REALTORS_LIST = reverse("estate:realtor-list")
HOUSE_LIST = reverse("estate:house-list")



class TestsForPublicRequired(TestCase):

    def test_login(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertNotEqual(response.status_code, 200)

    def test_realtor_list(self):
        response = self.client.get(REALTORS_LIST)
        self.assertNotEqual(response.status_code, 200)

    def test_house_list(self):
        response = self.client.get(HOUSE_LIST)
        self.assertNotEqual(response.status_code, 200)


class TestsForPrivateRequired(TestCase):
    def setUp(self) -> None:
        self.realtor = get_user_model().objects.create_user(
            username="test",
            password="dissom1987"
        )
        self.client.force_login(self.realtor)

    def test_login(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_driver_list(self):
        response = self.client.get(REALTORS_LIST)
        self.assertEqual(response.status_code, 200)

    def test_car_list(self):
        response = self.client.get(HOUSE_LIST)
        self.assertEqual(response.status_code, 200)
