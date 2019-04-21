"""S1C8. Detect AES in ECB mode."""

import binascii
import itertools

def detect():
  f = open('c08_detect_aes_in_ecb_mode_file', 'r')
  lines = [binascii.unhexlify(line.strip()) for line in f.readlines()]
  f.close()

  for line in lines:
    # Make 16 byte ciphertext blocks.
    blocks = [line[i:i + 16] for i in range(0, len(line), 16)]

    # Each pair of blocks has score 1 if the blocks are the same,
    # and 0 otherwise.
    score = [
        pair[0] == pair[1]
        for pair in itertools.combinations(blocks, 2)
    ].count(True)

    if score > 0:
      print(line)

if __name__ == '__main__':
  detect()