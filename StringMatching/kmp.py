# manan kher
def compute_prefix(pattern):
    m = len(pattern)
    prefix = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix[length - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    prefix = compute_prefix(pattern)
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = prefix[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return matches

# Example usage:
text = "AABAACAADAABAABA"
pattern = "AABA"
matches = kmp_search(text, pattern)
if matches:
    print("Pattern found at index(es):", matches)
else:
    print("Pattern not found in the text.")
