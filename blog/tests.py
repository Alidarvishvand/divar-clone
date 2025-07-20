from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from accounts.models import CustomUser

class PostAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email="admin@admin.com", password="123123aas")
        self.category = Category.objects.create(name="تست", slug="test-category")


        self.approved_post = Post.objects.create(
            user=self.user,
            category=self.category,
            title="پست تایید شده",
            description="توضیح",
            price=10000,
            is_approved=True
        )
        self.unapproved_post = Post.objects.create(
            user=self.user,
            category=self.category,
            title="پست تایید نشده",
            description="توضیح",
            price=20000,
            is_approved=False
        )

    def test_post_list_view(self):
        url = reverse("blog:post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  

    def test_post_detail_view(self):
        url = reverse("blog:post-detail", args=[self.approved_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.approved_post.title)

    def test_post_create_view_requires_authentication(self):
        url = reverse("blog:post-create")
        data = {
            "title": "پست جدید",
            "description": "یه پست تستی",
            "price": 15000,
            "province": "تهران",
            "category": self.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)  
    def test_post_create_with_authentication(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("blog:post-create")
        data = {
            "title": "پست جدید",
            "description": "یه پست تستی",
            "price": 15000,
            "province": "تهران",
            "category": self.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 3)

    def test_filtered_post_list(self):
        url = reverse("blog:post-list") + "?min_price=5000&max_price=15000&category=test-category"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
