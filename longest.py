import unittest


def longest(words):
    # Your solution here
    letter_numbers = [max(len(word) for word in words)]
    return letter_numbers[0]
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars:

    python -m unittest longest.TestLongest.test_ok

or

    pytest longest.py
"""


class TestLongest(unittest.TestCase):

    def test_ok(self):
        assert longest(['simple', 'is', 'better', 'than', 'complex']) == 7
        assert longest(['explicit', 'is', 'better', 'than', 'implicit']) == 8
        assert longest(['beautiful', 'is', 'better', 'than', 'ugly']) == 9


if __name__ == '__main__':
    unittest.main()
