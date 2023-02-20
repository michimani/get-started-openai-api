
import unittest
from collections import namedtuple
from token_count import tokens


class TestTokenCount(unittest.TestCase):
    """test class of token_count.py
    """

    def test_tokens(self):
        """test method for tokens
        """
        C = namedtuple("C", "msg text expect")
        cases = [
            C("English", "Hello OpenAI API.", [15496, 4946, 20185, 7824, 13]),
            C("Japanese", "こんにちは、 OpenAI API.", [
              46036, 22174, 28618, 2515, 94, 31676, 23513, 4946, 20185, 7824, 13]),
        ]

        for c in cases:
            with self.subTest(msg=c.msg):
                tks, count = tokens(c.text)
                self.assertEqual(c.expect, tks)
                self.assertEqual(len(c.expect), count)


if __name__ == "__main__":
    unittest.main()
