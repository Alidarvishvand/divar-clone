from django.urls import reverse
from rest_framework.test import APITestCase
from category.models import Category

class CategoryAPITests(APITestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name="سواری", slug="sor")


    def test_category_list(self):
        url = reverse("category:category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "سواری")

    def test_category_detail(self):
        url = reverse("category:category-detail", args=[self.cat1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["slug"], "sor")
