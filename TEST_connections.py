import unittest
import connections

board1 = {
    "FRUITS": ["APPLE", "BANANA", "CHERRY", "ORANGE"],
    "VEGETABLES": ["CARROT", "BROCCOLI", "SPINACH", "PEAS"]
}

class TestValidity(unittest.TestCase):
    def test_valid_1(self):
        '''Guesses are valid and match a category in the board'''
        guesses = ["APPLE", "BANANA", "CHERRY", "ORANGE"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, True)

    def test_valid_2(self):
        '''Guesses are valid and come from different categories'''
        guesses = ["APPLE", "CARROT", "SPINACH", "ORANGE"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, True)

    def test_invalid_1(self):
        '''Guess not on board'''
        guesses = ["APPLE", "BANANA", "CHERRY", "LAMP"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, False)

    def test_invalid_2(self):
        '''Less than 4 guesses'''
        guesses = ["APPLE", "BANANA", "CHERRY"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, False)

    def test_invalid_3(self):
        '''More than 4 guesses'''
        guesses = ["APPLE", "BANANA", "CHERRY", "ORANGE", "CARROT"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, False)

    def test_invalid_4(self):
        '''Non-unique guesses'''
        guesses = ["APPLE", "BANANA", "CHERRY", "APPLE"]

        actual = connections.validate_guess(guesses, board1)

        self.assertEqual(actual, False)

class TestCheckGuessCorrectness(unittest.TestCase):
    pass

class TestReadLine(unittest.TestCase):
    pass

class TestReadCategory(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()