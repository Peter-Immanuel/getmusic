import datetime
from multiprocessing.sharedctypes import Value
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserManagerTestCase(TestCase):
   
   def test_create_user(self):
      User = get_user_model()
      user = User.objects.create_user(
         email="testuser@gmail.com",
         first_name="Test", last_name="User",
         geek_name="TestUser",country="Nigeria",
         phone="+2348012345678",date_of_birth=datetime.date(1982,1,1),
         password="testpassword"
      )

      self.assertEqual(user.email, "testuser@gmail.com")
      self.assertEqual(user.geek_name, "TestUser")
      self.assertEqual(user.country, "Nigeria")
      self.assertFalse(user.is_active)
      self.assertFalse(user.is_staff)
      self.assertFalse(user.is_superuser)


      with self.assertRaises(TypeError):
         User.objects.create_user()
         User.objects.create_user(email="")

      with self.assertRaises(ValueError):
         User.objects.create_user(email="", password="")

   def test_create_superuser(self):
      User = get_user_model()
      admin_user = User.objects.create_superuser(
         email="admin@gmail.com",geek_name="adminTestUser",password="testpassword"
      )

      self.assertEqual(admin_user.email, "admin@gmail.com")
      self.assertFalse(admin_user.is_active)
      self.assertFalse(admin_user.is_staff)
      self.assertFalse(admin_user.is_superuser)

      with self.assertRaises(ValueError):
         User.objects.create_superuser(
            email="",geek_name="adminTestUser",password="testpassword",
            is_superuser=False
         )