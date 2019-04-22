"""S2C09. Implement PKCS#7 padding."""


def pad(text, block_size):
  """Pads byte string to indicated block size via pkcs7 padding."""

  len_to_pad = block_size - len(text) % block_size
  return text + bytes([len_to_pad] * len_to_pad)


def unpad(text):
  """Unpads byte string according to pkcs7."""

  pad_len = text[-1]
  for i in range(-1 * pad_len, -1):
    if text[i] != pad_len:
      raise Exception('Invalid padding')

  return text[:(-1 * pad_len)]
