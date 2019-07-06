from django.test import TestCase
from django.urls import reverse_lazy


# Create your tests here.
from account_mapping.models import AccountMapping, Mandator


class AccountMappingTestCase(TestCase):
    def test_mapping_with_mandator(self):
        print(reverse_lazy("account_mapping:map-submit-account"))
        response = self.client.post(reverse_lazy("account_mapping:map-submit-account"),
                                    data={"email": "blabla@bla.de", "url": "blabla.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mandator.objects.count(), 1)

    def test_mapping_with_mandator_email_is_unique(self):
        print(reverse_lazy("account_mapping:map-submit-account"))
        data = {"email": "blabla@bla.de", "url": "blabla.com"}
        response = self.client.post(reverse_lazy("account_mapping:map-submit-account"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mandator.objects.count(), 1)
        response = self.client.post(reverse_lazy("account_mapping:map-submit-account"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Mandator.objects.count(), 1)

    def test_single_account_can_have_multiple_mandators(self):
        print(reverse_lazy("account_mapping:map-submit-account"))
        data = {"email": "blabla@bla.de", "url": "blabla.com"}
        response = self.client.post(reverse_lazy("account_mapping:map-submit-account"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mandator.objects.count(), 1)
        data = {"email": "blabla@bla.de", "url": "google.com"}
        response = self.client.post(reverse_lazy("account_mapping:map-submit-account"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mandator.objects.count(), 2)
