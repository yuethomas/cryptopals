"""S1C06. Break repeating-key XOR."""

import base64

from set_1 import c03_single_byte_xor_cipher as single_byte_xor_cipher

def repeating_key_xor_decrypt(ciphertext):
  """Tries to decrypt ciphertext as a Vigenere cipher."""

  ct_len = len(ciphertext)

  # Determine key size.
  for keysize in range(2, 41):
    fragment1 = ciphertext[0 : keysize]
    fragment2 = ciphertext[keysize : 2 * keysize]
    fragment3 = ciphertext[2 * keysize : 3 * keysize]
    fragment4 = ciphertext[3 * keysize : 4 * keysize]

    avg_hamming_dist = (hamming(fragment1, fragment2) +
                        hamming(fragment2, fragment3) +
                        hamming(fragment3, fragment4)) / 3 / keysize

    print(keysize, avg_hamming_dist)

  # Interleave into blocks.
  keysize = 29
  blocks = [[] for i in range(keysize)]

  for i in range(ct_len):
    blocks[i % keysize].append(ciphertext[i])

  decrypted = [
      single_byte_xor_cipher.single_byte_xor_cipher(
          bytes(blocks[i]))[1]
      for i in range(keysize)
  ]

  # Deinterleave.
  out_str = []
  for i in range(len(decrypted[0])):
    for j in range(keysize):
      try:
        out_str.append(decrypted[j][i])
      except IndexError:
        pass

  print(bytes(out_str).decode('ascii'))


def hamming(bytes1, bytes2):
  """Calculates the Hamming distance between two bytes-es.

  If the bytes-es are of different lengths, trim the longer one.
  """

  def _byte_hamming(byte1, byte2):
    xor_bytes = byte1 ^ byte2
    one_bits = 0
    while xor_bytes > 0:
      if xor_bytes % 2 == 1:
        one_bits += 1
      xor_bytes = xor_bytes >> 1
    return one_bits

  return sum([_byte_hamming(byte1, byte2)
              for (byte1, byte2) in zip(bytes1, bytes2)])

if __name__ == '__main__':
  TEXT = ''.join([
      line.strip()
      for line in open('c06_repeating_key_xor_file', 'r')
  ])
  repeating_key_xor_decrypt(base64.b64decode(TEXT))
