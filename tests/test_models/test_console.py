#!/usr/bin/python3
""" """
import unittest


class TestConsole(unittest.TestCase):
    def test_do_create_no_params(self):
        """ Test 'create' command with no parameters """
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        self.assertTrue(len(storage.all("BaseModel")) != 0)
    
    def test_do_create_with_string_param(self):
        """ Test 'create' command with a string parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == "John Doe" for obj in objects.values()))

    def test_do_create_with_integer_param(self):
        """ Test 'create' command with an integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=30')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 30 for obj in objects.values()))

    def test_do_create_with_float_param(self):
        """ Test 'create' command with a float parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_invalid_param(self):
        """ Test 'create' command with an invalid parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel invalid_param')
        objects = storage.all("BaseModel")
        self.assertFalse(any('invalid_param' in obj.to_dict() for obj in objects.values()))

    def test_do_create_with_float_param(self):
        """ Test 'create' command with a float parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_invalid_param(self):
        """ Test 'create' command with an invalid parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel invalid_param')
        objects = storage.all("BaseModel")
        self.assertFalse(any('invalid_param' in obj.to_dict() for obj in objects.values()))\

    def test_do_create_multiple_params(self):
        """ Test 'create' command with multiple parameters """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_Doe" age=30 score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == "John Doe" and obj.age == 30 and obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_escaped_string(self):
        """ Test 'create' command with a string containing an escaped quote """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_\\"Doe\\"_Smith"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John "Doe" Smith' for obj in objects.values()))

    def test_do_create_with_nonexistent_class(self):
        """ Test 'create' command with a nonexistent class """
        console = HBNBCommand()
        console.onecmd('create NonexistentClass')
        self.assertTrue(len(storage.all("NonexistentClass")) == 0)

    def test_do_create_with_special_chars(self):
        """ Test 'create' command with a string containing special characters """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_@#%_Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John @#% Doe' for obj in objects.values()))

    def test_do_create_with_empty_string(self):
        """ Test 'create' command with an empty string parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel name=""')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == '' for obj in objects.values()))

    def test_do_create_with_spaces_in_string(self):
        """ Test 'create' command with a string containing spaces """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_ _Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John  Doe' for obj in objects.values()))

    def test_do_create_with_negative_integer(self):
        """ Test 'create' command with a negative integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=-30')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == -30 for obj in objects.values()))

    def test_do_create_with_zero_integer(self):
        """ Test 'create' command with a zero integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=0')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 0 for obj in objects.values()))

    def test_do_create_with_large_integer(self):
        """ Test 'create' command with a large integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=1000000')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 1000000 for obj in objects.values()))
