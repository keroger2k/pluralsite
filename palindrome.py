import unittest
import sys

def is_palindrome(number):
    """Checks to see if a number to see if it is a palindrome

    Args:
        number: The number to be analyzed.

    Raises:
        ValueError: If the number being sent in is not valid.

    Returns: A bool if the number is a palindrome
    """
    return str(number) == str(number)[::-1]


def get_lychrel_sequence(number):
    sequences = []
    result = 12
    i = 0
    while not is_palindrome(result):
        if i > 200:
            break
        reverse = int(str(number)[::-1])
        result = number + reverse
        sequences.append((number, reverse, result))
        i += 1
        number = result
    return sequences


class PalindromeTest(unittest.TestCase):

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        is_palindrome(5555)

    def test_is_palindrome_works(self):
        """Test to ensure prints forwards and backwards are identical."""
        self.assertFalse(is_palindrome(1234))
        self.assertTrue(is_palindrome(4114))

    def test_check_single_entry(self):
        result = get_lychrel_sequence(9008299)
        self.assertEqual(result[-1][2], 555458774083726674580862268085476627380477854555)

    # def test_have_fun(self):
    #     """Basic smoke test: does the function run."""
    #     max_len = 0
    #     starting_number = 0
    #     for i in range(1):
    #         result = get_lychrel_sequence(i)
    #         current_length = len(result)
    #         current_start_number = result[0][0]
    #         if len(result) > max_len and current_length != 201:
    #             max_len = current_length
    #             sys.stdout.write("New High! {0} @ {1}\n".format(max_len, current_start_number))
    #     self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
