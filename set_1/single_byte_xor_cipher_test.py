"""Test for single_byte_xor_cipher."""

import unittest

from set_1 import single_byte_xor_cipher


class TestSingleByteXorCipher(unittest.TestCase):
  """Test for single_byte_xor_cipher."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input_str = ('1b37373331363f78151b7f2b783431333d78397828372d363c7'
                 '8373e783a393b3736')
    output_str = 'Cooking MC\'s like a pound of bacon'
    self.assertEqual(
        single_byte_xor_cipher.single_byte_xor_cipher(input_str)[1],
        output_str)


if __name__ == '__main__':
  unittest.main()