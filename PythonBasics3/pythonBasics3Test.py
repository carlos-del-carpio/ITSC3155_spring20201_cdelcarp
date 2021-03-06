import unittest

import pythonBasics3


class TestPythonBasicsOne(unittest.TestCase):

    # Test case for ends_with_consonant
    def test_ends_with_consonant(self):
        self.assertEqual(pythonBasics3.ends_with_consonant("Once upon a dark, cold night"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("What did Steve just say"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("I once swam with sharks"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("Do I know how old you are you"), False)

        # Please add three more test cases following the order above
        self.assertEqual(pythonBasics3.ends_with_consonant("This is another test"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("Here is yet another one"), False)

        self.assertEqual(pythonBasics3.ends_with_consonant("And a third one for good luck"), True)

    # Test case for ends_with_number
    def test_ends_with_number(self):
        self.assertEqual(pythonBasics3.ends_with_number("What is 3/10"), True)

        self.assertEqual(pythonBasics3.ends_with_number("It was not a cat"), False)

        self.assertEqual(pythonBasics3.ends_with_number("I once swam with sharks"), False)

        self.assertEqual(pythonBasics3.ends_with_number("Blue plus purple equals 5"), True)

        # Please add three more test cases following the order above

        self.assertEqual(pythonBasics3.ends_with_number("I wonder how many more question I can come up with. 1 maybe 2"), True)

        self.assertEqual(pythonBasics3.ends_with_number("What number is the sky? Mario"), False)

        self.assertEqual(pythonBasics3.ends_with_number("How many people does it take to change a light bulb? 1"), True)

    # # Test case for binary_multiple_of_6
    # def test_binary_multiple_of_6(self):
    #     self.assertEqual(pythonBasics3.binary_multiple_of_6("100101"), False)
    #
    #     self.assertEqual(pythonBasics3.binary_multiple_of_6("110"), True)
    #
    #     self.assertEqual(pythonBasics3.binary_multiple_of_6("111111"), False)
    #
    #     self.assertEqual(pythonBasics3.binary_multiple_of_6("3"), False)


if __name__ == '__main__':
    unittest.main(verbosity=1)
