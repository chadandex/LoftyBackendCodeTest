from django.test import TestCase
from api_app.models import SomeKeys

from multiprocessing import Queue

from utils.key_helpers import increment_value_ten_seconds, increment_value_once


class TestKeys(TestCase):
    def setUp(self):
        SomeKeys.objects.create(name='Nunya', default_value=1)
        SomeKeys.objects.create(name="Omega Key", default_value=2)
        SomeKeys.objects.create(name="Giga Key", default_value=3)

    def test_creating_dog(self):
        test_key = SomeKeys.objects.get(default_value=1)
        key_name = 'Nunya'

        self.assertEqual(test_key.name, key_name)

        print("Passed.")

    def test_incrementing(self):
        Q = Queue()
        increment_value = 1
        first_key = SomeKeys.objects.get(name="Omega Key")
        second_key = SomeKeys.objects.get(name="Giga Key")

        first_key_value = first_key.default_value
        increment_value_once(first_key, increment_value, Q)
        first_key_value_changed = first_key.default_value

        self.assertGreaterEqual(first_key_value_changed, first_key_value)

        second_key_value = second_key.default_value
        # may cause BrokenPipeError TODO: fix
        increment_value_ten_seconds(second_key, increment_value, Q)
        second_key_value_changed = second_key.default_value

        self.assertGreaterEqual(second_key_value_changed, second_key_value)

        Q.close()

        print("Passed.")
