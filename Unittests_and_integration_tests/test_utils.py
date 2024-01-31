#!/usr/bin/env python3
""" Test utils from utils.py """
import unittest
from unittest.mock import patch
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
        Test access nested map with unittest and parameterized
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
            Test access nested map
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
            Test access nested map throws KeyError when given invalid input
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
        Test get_json with mock patch
    """

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """
            Test get_json using mock patch to mock requests.get()
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"payload": True}
        self.assertEqual(utils.get_json(
            "http://example.com"), {"payload": True})
        mock_get.assert_called_once_with("http://example.com")

        mock_get.reset_mock()

        mock_get.return_value.json.return_value = {"payload": False}
        self.assertEqual(utils.get_json(
            "http://holberton.io"), {"payload": False})
        mock_get.assert_called_once_with("http://holberton.io")


class TestMemoize(unittest.TestCase):
    """
        Test memoize with unittest.mock.patch
    """

    def test_memoize(self):
        """
            Create a test class and test memoize()
        """
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()
