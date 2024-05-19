
###
# K4 ciphertext
# ciphertext = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
###

def encrypt_caesar(plaintext, shift):
    """
    Encrypts a plaintext using a Caesar cipher with a specified shift value.
    Args:
        plaintext (str): The original message.
        shift (int): The shift value (0-25).
    Returns:
        str: The encrypted ciphertext.
    """
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character forward by the specified amount
            shifted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    """
    Decrypts a Caesar cipher ciphertext using a specified shift value.
    Args:
        ciphertext (str): The encrypted message.
        shift (int): The shift value (0-25).
    Returns:`
        str: The decrypted plaintext.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back by the specified amount
            shifted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

# Example usage
# plaintext = "Hello, World!"
# shift_value = 3
# ciphertext = encrypt_caesar(plaintext, shift_value)
# print("Encrypted text:", ciphertext)

# plaintext = decrypt_caesar(ciphertext, shift_value)
# print("Decrypted text:", plaintext)