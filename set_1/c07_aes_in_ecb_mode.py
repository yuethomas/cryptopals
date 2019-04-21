"""S1C07. AES in ECB mode."""

import base64

from cryptography.hazmat import backends
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import modes


def decrypt_aes_ecb(ciphertext, key):
  """Decrypts the ciphertext in the file with known key."""
  cipher = ciphers.Cipher(
      algorithms.AES(key),
      modes.ECB(),
      backends.default_backend())
  decryptor = cipher.decryptor()
  plaintext = decryptor.update(ciphertext) + decryptor.finalize()
  return plaintext.decode('ascii')


if __name__ == '__main__':
  CIPHERTEXT = base64.b64decode(''.join([
      line.strip()
      for line in open('c07_aes_in_ecb_mode_file', 'r')
  ]))
  KEY = 'YELLOW SUBMARINE'.encode('ascii')
  print(decrypt_aes_ecb(CIPHERTEXT, KEY))
