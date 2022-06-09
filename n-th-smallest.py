import unittest


def nth_smallest(arr, pos):
    # Your code here
    arr.sort()
    return arr[pos-1]
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars:

    python -m unittest n-th-smallest.TestNthSmallest.test_ok

or

    python n-th-smallest.py
"""


class TestNthSmallest(unittest.TestCase):

    def test_ok(self):
        assert nth_smallest([3, 1, 2], 2) == 2
        assert nth_smallest([15, 20, 7, 10, 4, 3], 3) == 7
        assert nth_smallest([-5, -1, -6, -18], 4) == -1
        assert nth_smallest([-102, -16, -1, -2, -367, -9], 5) == -2
        assert nth_smallest([2, 169, 13, -5, 0, -1], 4) == 2


if __name__ == '__main__':
    unittest.main()
