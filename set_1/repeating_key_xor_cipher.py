"""S1C5. Repeating-key XOR."""

def repeating_key_xor_cipher(plaintext, cipher):
  """Encodes plaintext with cipher. Both inputs are bytearrays."""

  return bytearray([
      plaintext[i] ^ cipher[i % len(cipher)]
      for i in range(len(plaintext))
  ])
