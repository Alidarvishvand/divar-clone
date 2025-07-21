from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import Post, Category
from accounts.models import CustomUser
from chat.models import ChatMessage 

class ChatAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='admin@admin.com', password='123123aass')
        self.category = Category.objects.create(name="دیجیتال", slug="digital")
        self.post = Post.objects.create(
            user=self.user,
            category=self.category,
            title="آگهی تست",
            description="توضیحات",
            price=10000,
            province="تهران",
            is_approved=True
        )
        self.chat_url = reverse("chat:post-chat", kwargs={"post_id": self.post.id})

    def test_get_chat_list(self):
        self.client.force_authenticate(user=self.user)  
        response = self.client.get(self.chat_url)
        self.assertEqual(response.status_code, 200)

    def test_create_chat_requires_authentication(self):
        data = {"message": "سلام، این آگهی هنوز موجوده؟"}
        response = self.client.post(self.chat_url, data)
        self.assertEqual(response.status_code, 403)  

    def test_create_chat_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"message": "سلام، این آگهی هنوز هست؟"}
        response = self.client.post(self.chat_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ChatMessage.objects.count(), 1)
