from django.test import TestCase
from api_app.models import DogsModel


class TestDogs(TestCase):
    def setUp(self):
        DogsModel.objects.create(default_value=1, description='This is a test', imgsrc='test.jpg')

    def test_creating_dog(self):
        dog = DogsModel.objects.get(default_value=1)
        desc = 'This is a test'
        imgsrc = 'test.jpg'

        self.assertEqual(dog.description, desc)
        self.assertEqual(dog.imgsrc, imgsrc)

        print("Passed")
