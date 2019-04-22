"""Test for repeating_key_xor_cipher."""

import unittest

import binascii
from set_1 import (
    c05_repeating_key_xor_cipher as repeating_key_xor_cipher)


class TestRepeatingKeyXorCipher(unittest.TestCase):
  """Test for repeating_key_xor_cipher."""

  def test_predefined_string(self):
    """The test specified by CryptoPals."""

    input_str = ('Burning \'em, if you ain\'t quick and nimble\n'
                 'I go crazy when I hear a cymbal').encode('ascii')
    input_key = b'ICE'
    output_bin = binascii.unhexlify(
        '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26'
        '226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c'
        '692b20283165286326302e27282f')

    self.assertEqual(
        repeating_key_xor_cipher.repeating_key_xor_cipher(
            input_str, input_key),
        output_bin)

if __name__ == '__main__':
  unittest.main()
