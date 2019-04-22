"""S1C01. convert a hex string to a base64 string."""

_BASE64_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy'
                 'z0123456789+/')

def hex_to_base64(hexstring):
  """Converts hex in string format to base64 in string format."""

  return bytes_to_base64(hex_string_to_bytes(hexstring))

def hex_string_to_bytes(hexstring):
  """Converts hex in string format to a bytes object."""

  def _hex_nibble_to_value(nibble):
    char_val = ord(nibble)
    if char_val >= 48 and char_val <= 57:
      return char_val - 48
    if char_val >= 65 and char_val <= 70:
      return char_val - 55
    if char_val >= 97 and char_val <= 102:
      return char_val - 87
    raise "invalid hex!"

  return bytes([
      _hex_nibble_to_value(hexstring[i]) * 16 +
      _hex_nibble_to_value(hexstring[i + 1])
      for i in range(0, len(hexstring), 2)
  ])


def bytes_to_base64(bytestring):
  """Converts a bytes object to its base64 representation."""

  def _translate_6_bits(index):
    byte_ptr = index >> 3
    byte_offset = index - (byte_ptr << 3)
    cur_byte = bytestring[byte_ptr]
    if byte_offset <= 2:
      return (cur_byte >> (2 - byte_offset)) & 63

    if byte_ptr == len(bytestring) - 1:
      next_byte = 0
    else:
      next_byte = bytestring[byte_ptr + 1]

    shift_by = 8 - byte_offset
    return (((cur_byte & ((1<<shift_by) - 1)) << (byte_offset - 2)) +
            ((next_byte >> (shift_by + 2))))

  bit_pointer = 0
  bit_len = len(bytestring) * 8
  out = ''
  while bit_pointer < bit_len:
    out += _BASE64_CHARS[_translate_6_bits(bit_pointer)]
    bit_pointer = bit_pointer + 6
    if bit_pointer == bit_len + 2:
      out += '='
    elif bit_pointer == bit_len + 4:
      out += '=='

  return out
