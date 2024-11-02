from django.test import TestCase
from restaurant.models import Menu
# from  restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='test_a', price=1, inventory=1,)
        Menu.objects.create(title='test_b', price=2, inventory=2,)
        Menu.objects.create(title='test_c', price=3, inventory=3,)

    def test_getall(self):
        test_a = Menu.objects.get(title='test_a')
        test_b = Menu.objects.get(title='test_b')
        test_c = Menu.objects.get(title='test_c')
        self.assertEqual(test_a.__str__(), "test_a : 1.00")
        self.assertEqual(test_b.__str__(), "test_b : 2.00")
        self.assertEqual(test_c.__str__(), "test_c : 3.00")