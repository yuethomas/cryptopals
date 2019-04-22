"""S2C10. Implement CBC mode."""

import base64

from set_1 import c02_fixed_xor as xor
from set_1 import c07_aes_in_ecb_mode as aes_ecb
from set_2 import c09_pkcs7_padding as pkcs7_padding


BLOCK_SIZE = 16


def aes_cbc(text, key, iv, encrypt=False):  # pylint: disable=invalid-name
  """Encrypts or decrypts using AES in CBC mode."""

  # Make len(key) byte ciphertext blocks.
  blocks = [
      text[i:i + BLOCK_SIZE]
      for i in range(0, len(text), BLOCK_SIZE)
  ]

  state = iv
  out_blocks = b''
  for block in blocks:
    out_blocks += xor.fixed_xor(
        state,
        aes_ecb.aes_ecb(block, key, encrypt=encrypt))
    state = block

  return pkcs7_padding.unpad(out_blocks)


if __name__ == '__main__':
  TEXT = base64.b64decode(''.join([
      line.strip()
      for line in open('c10_aes_in_cbc_mode_file', 'r')
  ]))
  KEY = b'YELLOW SUBMARINE'
  IV = bytes(BLOCK_SIZE)

  print(aes_cbc(TEXT, KEY, IV, encrypt=False).decode('ascii'))
