"""Tests for hex_to_base64."""

import base64
import binascii
import random
import unittest

from set_1 import c01_hex_to_base64 as hex_to_base64


class TestHexToBase64(unittest.TestCase):
  """Tests for hex_to_base64."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input_str = ('49276d206b696c6c696e6720796f757220627261696e206c696'
                 'b65206120706f69736f6e6f7573206d757368726f6f6d')
    output_str = ('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3'
                  'VzIG11c2hyb29t')
    self.assertEqual(
        hex_to_base64.hex_to_base64(input_str), output_str)

  def test_random_string_100_times(self):
    """Generates 100 random hex strings to test."""

    for _ in range(100):
      input_str = random_hex_string()
      output_str = base64.b64encode(
          binascii.unhexlify(input_str)).decode('ascii')
      self.assertEqual(
          hex_to_base64.hex_to_base64(input_str), output_str)


def random_hex_string():
  """Generates random hex string."""

  corpus = '0123456789abcdef'
  min_len = 10
  max_len = 100
  str_len = random.randrange(min_len, max_len + 1, 2)
  return ''.join([
      corpus[random.randrange(0, len(corpus))]
      for _ in range(str_len)
  ])


if __name__ == '__main__':
  unittest.main()
