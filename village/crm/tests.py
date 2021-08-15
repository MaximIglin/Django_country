from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model
from . models import village_data, layout_data, Regions

User = get_user_model()

class CrmTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username = 'TestUser', password = 'password')
        return super().setUp()


#git commit test