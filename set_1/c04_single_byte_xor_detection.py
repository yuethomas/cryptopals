"""S1C04. Given a file, determine which line has been encrypted."""

import binascii
from set_1 import c03_single_byte_xor_cipher as single_byte_xor_cipher


def single_byte_xor_detection(line):
  """Determines if a line has been encrypted by a xor cipher."""
  try:
    decryption = single_byte_xor_cipher.single_byte_xor_cipher(
        binascii.unhexlify(line))
    if decryption[1]:
      print(decryption[1].decode('ascii'))
  except UnicodeDecodeError:
    pass


if __name__ == '__main__':
  for xor_line in open('c04_single_byte_xor_list', 'r'):
    single_byte_xor_detection(xor_line.strip())
