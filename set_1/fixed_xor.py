"""S1C2: take two equal length buffers and produces their XOR."""

import binascii


def fixed_xor(str1, str2):
  """Takes two equal length strings and producesa their XOR."""

  bytearray1 = binascii.unhexlify(str1)
  bytearray2 = binascii.unhexlify(str2)

  out = bytearray([
      byte1 ^ byte2 for (byte1, byte2)
      in zip(bytearray1, bytearray2)])

  return binascii.hexlify(out).decode('ascii')
