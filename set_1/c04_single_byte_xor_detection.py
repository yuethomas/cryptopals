"""S1C04. Given a file, determine which line has been encrypted."""

import binascii
from set_1 import c03_single_byte_xor_cipher as single_byte_xor_cipher


def single_byte_xor_detection(list_of_encrypted_text):
  """Given a file, determines which line has been encrypted."""
  for line in list_of_encrypted_text:
    try:
      decryption = single_byte_xor_cipher.single_byte_xor_cipher(
          bytearray(binascii.unhexlify(line.strip())))
      if decryption[1]:
        print(decryption[1].decode('ascii'))
    except UnicodeDecodeError:
      continue

if __name__ == '__main__':
  ENC_FILE = open('c04_single_byte_xor_list', 'r')
  single_byte_xor_detection(ENC_FILE.readlines())
  ENC_FILE.close()
