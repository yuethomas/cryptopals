"""Tests for aes_in_ecb_mode."""

import unittest

from set_1 import c07_aes_in_ecb_mode as aes_in_ecb_mode


class TestAesInEcbMode(unittest.TestCase):
  """Tests for aes_in_ecb_mode."""

  def test_encrypt_decrypt(self):
    """Test that encrypt then decrypts the same string."""

    input_str = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 'abcdefghijklmnopqrstuvwxyz'
                 '1234567890-=').encode('ascii')

    key = b'YELLOW SUBMARINE'

    self.assertEqual(
        aes_in_ecb_mode.aes_ecb(
            aes_in_ecb_mode.aes_ecb(input_str, key, encrypt=True),
            key,
            encrypt=False),
        input_str)


if __name__ == '__main__':
  unittest.main()
