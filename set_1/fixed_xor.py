"""S1C2: take two equal length buffers and produces their XOR."""


def fixed_xor(bytearray1, bytearray2):
  """Takes two equal length bytearrays and produces their XOR."""

  return bytearray([
      byte1 ^ byte2 for (byte1, byte2)
      in zip(bytearray1, bytearray2)])
