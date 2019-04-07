"""S1C4. Given a file, determine which line has been encrypted."""

from set_1 import single_byte_xor_cipher


def single_byte_xor_detection(list_of_encrypted_text):
  """Given a file, determines which line has been encrypted."""
  for line in list_of_encrypted_text:
    try:
      decryption = single_byte_xor_cipher.single_byte_xor_cipher(
          line.strip())
      if decryption:
        print decryption
    except UnicodeDecodeError:
      continue

if __name__ == '__main__':
  ENC_FILE = open('single_byte_xor_list', 'r')
  single_byte_xor_detection(ENC_FILE.readlines())
  ENC_FILE.close()
