"""S1C05. Repeating-key XOR."""

def repeating_key_xor_cipher(plaintext, cipher):
  """Encodes plaintext with cipher. Both inputs are bytes."""

  return bytes([
      plaintext[i] ^ cipher[i % len(cipher)]
      for i in range(len(plaintext))
  ])
