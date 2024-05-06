
# d is the number of characters in the input alphabet
ALPHABET_SIZE = 256

# pattern -> patternrn_text
# text -> main_text
# prime -> A prime number


def rabin_karp_search(pattern_text, main_text, prime):
    pattern_length = len(pattern_text)
    main_text_length = len(main_text)
    i = 0
    j = 0
    pattern_hash = 0
    main_text_hash = 0
    hash_multiplier = 1

    # The value of hash_multiplier would be "pow(ALPHABET_SIZE, pattern_length-1)%prime"
    for i in range(pattern_length-1):
        hash_multiplier = (hash_multiplier * ALPHABET_SIZE) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(pattern_length):
        pattern_hash = (ALPHABET_SIZE * pattern_hash + ord(pattern_text[i])) % prime
        main_text_hash = (ALPHABET_SIZE * main_text_hash + ord(main_text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(main_text_length-pattern_length+1):
        # Check the hash values of current window of text and pattern
        # if the hash values match then only check for characters one by one
        if pattern_hash == main_text_hash:
            # Check for characters one by one
            for j in range(pattern_length):
                if main_text[i+j] != pattern_text[j]:
                    break
                else:
                    j += 1

            # if pattern_hash == main_text_hash and pattern_text[0...pattern_length-1] = main_text[i, i+1, ...i+pattern_length-1]
            if j == pattern_length:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove leading character, add trailing character
        if i < main_text_length - pattern_length:
            main_text_hash = (ALPHABET_SIZE * (main_text_hash - ord(main_text[i]) * hash_multiplier) + ord(main_text[i + pattern_length])) % prime

            # We might get negative values of main_text_hash, converting it to positive
            if main_text_hash < 0:
                main_text_hash = main_text_hash + prime


# Driver Code
if __name__ == '__main__':
    main_text = "AABAACAADAABAABA"
    pattern_text = "AABA"

    # A prime number
    prime = 101

    # Function Call
    rabin_karp_search(pattern_text, main_text, prime)


