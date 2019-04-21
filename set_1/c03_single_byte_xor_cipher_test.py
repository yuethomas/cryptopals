"""Test for single_byte_xor_cipher."""

import unittest

import binascii
from set_1 import c03_single_byte_xor_cipher as single_byte_xor_cipher


class TestSingleByteXorCipher(unittest.TestCase):
  """Test for single_byte_xor_cipher."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input_str = bytearray(binascii.unhexlify(
        '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a'
        '393b3736'))
    output_str = 'Cooking MC\'s like a pound of bacon'
    self.assertEqual(
        single_byte_xor_cipher.single_byte_xor_cipher(
            input_str)[1].decode('ascii'),
        output_str)


if __name__ == '__main__':
  unittest.main()
