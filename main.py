import random
import string

secret_message = "Somewhere over the rainbow 1223"
number = 3

def random_char():
    # Randomly choose between lowercase, uppercase, or digit
    choice = random.choice(['lower', 'upper', 'digit'])
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    elif choice == 'upper':
        return random.choice(string.ascii_uppercase)
    elif choice == 'digit':
        return random.choice(string.digits)

def caesar_cipher(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.islower():
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            result.append((new_char, random_char()))  # Store original and random char
        elif char.isupper():
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            result.append((new_char, random_char()))  # Store original and random char
        elif char.isdigit():
            new_char = chr((ord(char) + shift - 48) % 10 + 48)
            result.append((new_char, random_char()))  # Store original and random char
        else:
            result.append((char, char))  # Non-alphanumeric characters remain unchanged

    # Create the final encrypted string using random characters
    encrypted_message = ''.join([rand for _, rand in result])
    return encrypted_message, result  # Return encrypted message and original data for decryption

def caesar_decipher(encrypted_message: str, original_data: list, shift: int) -> str:
    result = []

    for i, char in enumerate(encrypted_message):
        if char.islower() or char.isupper() or char.isdigit():
            original_char = original_data[i][0]  # Retrieve the original character
            result.append(original_char)
        else:
            result.append(char)  # Non-alphanumeric characters remain unchanged

    # Apply left shift to the decrypted message
    final_decrypted_message = []
    for char in result:
        if char.islower():
            shifted_char = chr((ord(char) - shift - 97) % 26 + 97)
            final_decrypted_message.append(shifted_char)
        elif char.isupper():
            shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
            final_decrypted_message.append(shifted_char)
        elif char.isdigit():
            shifted_char = chr((ord(char) - shift - 48) % 10 + 48)
            final_decrypted_message.append(shifted_char)
        else:
            final_decrypted_message.append(char)  # Non-alphanumeric characters remain unchanged

    return ''.join(final_decrypted_message)

# Encrypt the message
hidden_message, original_data = caesar_cipher(secret_message, number)
print("Encrypted:", hidden_message)

# Decrypt the message and apply left shift
decrypted_message = caesar_decipher(hidden_message, original_data, number)
print("Final Decrypted (after left shift):", decrypted_message)