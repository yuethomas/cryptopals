"""S1C07. AES in ECB mode."""

import base64

from cryptography.hazmat import backends
from cryptography.hazmat.primitives import ciphers

key = 'YELLOW SUBMARINE'.encode('ascii')

def decrypt():
  FILE = open('c07_aes_in_ecb_mode_file', 'r')
  b64 = ''.join([line.strip() for line in FILE.readlines()])
  FILE.close()

  ciphertext = base64.b64decode(b64)
  cipher = ciphers.Cipher(
      ciphers.algorithms.AES(key),
      ciphers.modes.ECB(),
      backends.default_backend())
  decryptor = cipher.decryptor()
  plaintext = decryptor.update(ciphertext) + decryptor.finalize()
  return plaintext


if __name__ == '__main__':
  print(decrypt())
