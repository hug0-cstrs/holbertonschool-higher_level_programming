import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test when list_dictionaries is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list_dictionaries is not empty
        list_dicts = [{"key": "value"}, {"key2": "value2"}]
        expected_output = '[{"key": "value"}, {"key2": "value2"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_output)

    def test_save_to_file(self):
        # Test when list_objs is None
        Base.save_to_file(None)
        self.assertFalse(os.path.exists("Base.json"))

        # Test when list_objs is empty
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))

        # Test when list_objs contains objects
        rectangle = Rectangle(1, 2)
        square = Square(3)
        Base.save_to_file([rectangle, square])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            file_content = file.read()

    def test_from_json_string(self):
        # Test when json_string is None
        self.assertEqual(Base.from_json_string(None), [])

        # Test when json_string is empty
        self.assertEqual(Base.from_json_string(""), [])

        # Test when json_string contains valid JSON
        json_string = '[{"key": "value"}, {"key2": "value2"}]'
        expected_output = [{"key": "value"}, {"key2": "value2"}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    # Add more test methods for other methods in the Base class


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_perimeter(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.perimeter(), 18)

    def test_display(self):
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update(self):
        rectangle = Rectangle(2, 4)
        rectangle.update(5, 6, 7, 8)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 8)
        self.assertEqual(rectangle.y, 0)

    class TestSquare(unittest.TestCase):
        def test_area(self):
            square = Square(5)
            self.assertEqual(square.area(), 25)

        def test_perimeter(self):
            square = Square(5)
            self.assertEqual(square.perimeter(), 20)

        def test_display(self):
            square = Square(3)
            expected_output = "###\n###\n###\n"
            with patch("sys.stdout", new=StringIO()) as fake_out:
                square.display()
                self.assertEqual(fake_out.getvalue(), expected_output)

        def test_update(self):
            square = Square(4)
            square.update(5, 6, 7, 8)
            self.assertEqual(square.size, 6)
            self.assertEqual(square.x, 7)
            self.assertEqual(square.y, 8)

    if __name__ == '__main__':
        unittest.main()
