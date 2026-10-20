from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class CustomUserManagerTests(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(email='user@example.com', password='pass12345')
        self.assertEqual(user.email, 'user@example.com')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('pass12345'))
        self.assertEqual(str(user), 'user@example.com')

    def test_create_user_without_email_raises(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email='', password='pass12345')
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email=None, password='pass12345')

    def test_email_is_normalized(self):
        user = self.User.objects.create_user(email='Test@EXAMPLE.COM', password='pass12345')
        self.assertEqual(user.email, 'Test@example.com')

    def test_create_superuser(self):
        admin = self.User.objects.create_superuser(email='admin@example.com', password='pass12345')
        self.assertEqual(admin.email, 'admin@example.com')
        self.assertTrue(admin.is_superuser)

    def test_create_superuser_invalid_flags(self):
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='admin@example.com', password='pass12345', is_superuser=False)
