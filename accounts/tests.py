from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import CustomUser,Profile
from rest_framework_simplejwt.tokens import RefreshToken


class AccountsAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            phone="09120000000",
            password="pass1234",
            first_name="Ali",
            last_name="Testi"
        )
        Profile.objects.create(user=self.user)  # ← همین خط باعث رفع ارور میشه

        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:token_obtain_pair")
        self.profile_url = reverse("accounts:user-profile")
        self.logout_url = reverse("accounts:logout")
        self.refresh_url = reverse("accounts:token_refresh")
        self.change_password_url = reverse("accounts:change_password", args=[self.user.id])
    def test_register(self):
        data = {
            "email": "new@example.com",
            "phone": "09121111111",
            "first_name": "Sara",
            "last_name": "Karimi",
            "password": "newpass1234",
            "confirm_password": "newpass1234"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("user", response.data)

    def test_login_and_get_token(self):
        data = {
            "email": "test@example.com",
            "password": "pass1234"
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.access_token = response.data["access"]
        self.refresh_token = response.data["refresh"]

    def test_profile_requires_authentication(self):
        response = self.client.get(self.profile_url)
        # ممکنه 403 یا 401 بده بسته به نوع احراز هویت
        self.assertIn(response.status_code, [401, 403])

    def test_profile_with_token(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_change_password(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "old_password": "pass1234",
            "new_password": "newpassword456"
        }
        response = self.client.put(self.change_password_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("success", response.data)

    def test_token_refresh(self):
        token = RefreshToken.for_user(self.user)
        refresh_token = str(token)
        response = self.client.post(self.refresh_url, {"refresh": refresh_token})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_logout(self):
        refresh = RefreshToken.for_user(self.user)
        data = {"refresh": str(refresh)}
        response = self.client.post(self.logout_url, data)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
