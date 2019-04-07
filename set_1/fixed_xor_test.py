"""Tests for fixed_xor."""

import unittest

from set_1 import fixed_xor


class TestFixedXor(unittest.TestCase):
  """Tests for fixed_xor."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    output = '746865206b696420646f6e277420706c6179'
    self.assertEqual(fixed_xor.fixed_xor(input1, input2), output)


if __name__ == '__main__':
  unittest.main()
