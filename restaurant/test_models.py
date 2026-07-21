from django.test import TestCase
from .models import Menu


class MenuModelTest(TestCase):

    def test_menu_creation(self):
        item = Menu.objects.create(
            title="Pizza",
            price=299,
            inventory=20
        )

        self.assertEqual(item.title, "Pizza")