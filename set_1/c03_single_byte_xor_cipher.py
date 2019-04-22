"""S1C03. Decodes a hex-encoded string as a single byte XOR cipher."""

# Frequency distribution of English letters according to Wikipedia.
# Use this as a score. The last one is for space.
_EN_FREQ_DIST = [x / 0.1918182 for x in [
    0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881,
    0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490,
    0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563,
    0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692,
    0.0145984, 0.0007836, 0.1918182]]


def single_byte_xor_cipher(bytestring):
  """Decodes bytes as a single byte XOR cipher."""
  cipher_scores = []

  for cipher in range(128):
    dist = [0] * 27
    discarded = 0

    for original_byte in bytestring:
      byte = original_byte ^ cipher
      if byte >= 65 and byte <= 90:
        dist[byte - 65] += 1

      elif byte >= 97 and byte <= 122:
        dist[byte - 97] += 1

      elif byte == 32:
        # space
        dist[26] += 1

      else:
        discarded += 1

    # heuristic; discarded characters should not exceed 20% of the
    # entire string size.
    if discarded > len(bytestring) / 2:
      continue

    # calculate distribution, with most frequent element as 1
    dist = [d / max(dist) for d in dist]

    cipher_scores.append((cipher, sum([
        abs(a - b) for (a, b) in zip(_EN_FREQ_DIST, dist)])))

  cipher_scores.sort(key=lambda c: c[1])

  for (cipher, score) in cipher_scores:
    return (score, bytes([b ^ cipher for b in bytestring]))

  return (None, None)
