def vigenere_encrypt(plain_text, key):
    """
    Encrypts a message using the Vigenère cipher.
    Args:
        plain_text (str): The original message.
        key (str): The keyword or phrase used as the key.
    Returns:
        str: The encrypted ciphertext.
    """
    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key_repeated[i].lower()) - ord('a')
            shifted_char = chr(((ord(plain_text[i].lower()) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += shifted_char.upper() if plain_text[i].isupper() else shifted_char
        else:
            encrypted_text += plain_text[i]

    return encrypted_text

def vigenere_crack(ciphertext):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tetrafrequencies = [0] * 26**4

    # Calculate tetragram frequencies
    for i in range(len(ciphertext) - 3):
        tetra_index = sum(ALPHABET.index(c) * 26**(3 - j) for j, c in enumerate(ciphertext[i:i + 4]))
        tetrafrequencies[tetra_index] += 1

    # Normalize frequencies
    total_tetras = len(ciphertext) - 3
    tetrafrequencies = [freq / total_tetras for freq in tetrafrequencies]

    # Find the most likely tetragram
    max_freq = max(tetrafrequencies)
    likely_tetra_index = tetrafrequencies.index(max_freq)

    # Convert tetragram index to key
    likely_key = ''.join(ALPHABET[i] for i in divmod(likely_tetra_index, 26**3))

    return likely_key

# Example usage
ciphertext = "bldori"
likely_key = vigenere_crack(ciphertext)
print("Likely key:", likely_key)
