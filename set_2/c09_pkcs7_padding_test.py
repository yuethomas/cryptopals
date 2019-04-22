"""Test for pkcs7_padding."""

import unittest

from set_2 import c09_pkcs7_padding as pkcs7_padding


class TestPkcs7Padding(unittest.TestCase):
  """Test for pkcs7_padding."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input_str = b'YELLOW SUBMARINE'
    block_size = 10
    output_str = b'YELLOW SUBMARINE\x04\x04\x04\x04'

    self.assertEqual(
        pkcs7_padding.pad(input_str, block_size),
        output_str)

  def test_block_size_pad(self):
    """Test that pads the full block size."""

    input_str = b'YELLOW SUBMARINE'
    block_size = 16
    output_str = b'YELLOW SUBMARINE' + bytes(
        [block_size] * block_size)
    self.assertEqual(
        pkcs7_padding.pad(input_str, block_size),
        output_str)

  def test_unpad(self):
    """Test for unpadding."""

    input_str = b'YELLOW SUBMARINE'
    block_size = 10
    self.assertEqual(
        pkcs7_padding.unpad(pkcs7_padding.pad(input_str, block_size)),
        input_str)

  def test_unpad_invalid(self):
    """Test for invalid padding."""

    input_str = b'YELLOW SUBMARINE\x02'
    self.assertRaises(Exception, pkcs7_padding.unpad, input_str)


if __name__ == '__main__':
  unittest.main()
