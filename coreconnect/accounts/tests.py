from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(phone_number='normal@user.com', first_name='john', last_name='pantau')
        self.assertEqual(user.phone_number, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(phone_number='')
        with self.assertRaises(ValueError):
            User.objects.create_user(phone_number='', first_name='john', last_name='pantau')
        with self.assertRaises(ValueError):
            User.objects.create_user(phone_number='', first_name='', last_name='pantau')
        with self.assertRaises(ValueError):
            User.objects.create_user(phone_number='', first_name='', last_name='')