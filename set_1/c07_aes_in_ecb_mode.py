"""S1C07. AES in ECB mode."""

import base64

from cryptography.hazmat import backends
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import modes


def aes_ecb(text, key, encrypt=False):
  """Decrypts the ciphertext in the file with known key."""
  cipher = ciphers.Cipher(
      algorithms.AES(key),
      modes.ECB(),
      backends.default_backend())
  cryptor = cipher.encryptor() if encrypt else cipher.decryptor()
  crypt = cryptor.update(text) + cryptor.finalize()
  return crypt


if __name__ == '__main__':
  CIPHERTEXT = base64.b64decode(''.join([
      line.strip()
      for line in open('c07_aes_in_ecb_mode_file', 'r')
  ]))
  KEY = b'YELLOW SUBMARINE'
  print(aes_ecb(CIPHERTEXT, KEY).decode('ascii'))
