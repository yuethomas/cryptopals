"""Tests for repeating_key_xor_decrypt."""

import unittest

from set_1 import (
    c06_repeating_key_xor_decrypt as repeating_key_xor_decrypt)


class TestRepeatingKeyXorDecrypt(unittest.TestCase):
  """Tests for repeating_key_xor_decrypt."""

  def test_hamming_predefined_string(self):
    """Test for Hamming, specified by CryptoPals."""
    input_str1 = bytearray(b'this is a test')
    input_str2 = bytearray(b'wokka wokka!!!')
    output = 37
    self.assertEqual(
        repeating_key_xor_decrypt.hamming(input_str1, input_str2),
        output)


if __name__ == '__main__':
  unittest.main()
