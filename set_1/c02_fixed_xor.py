"""S1C02. take two equal length buffers and produces their XOR."""


def fixed_xor(bytes1, bytes2):
  """Takes two equal length bytes and produces their XOR."""

  return bytes([
      byte1 ^ byte2
      for (byte1, byte2) in zip(bytes1, bytes2)
  ])
