import unittest

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()


# Test Results:
# The test passed successfully. The result of adding
# the numbers 1, 2, and 3 was 6, which matched the
# expected result. This means the sum function worked
# correctly with the list of integers that I tested.
# The test runner reported one successful test and
# no failures or errors.