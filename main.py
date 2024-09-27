secret_message = "Somewhere over the rainbow"
number = 3

def caesar_cipher(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char

    return result

def caeser_decipher(secret_message:str, shift: int):
    result = ""

    for char in secret_message:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char

    return result

hidden_message = caesar_cipher(secret_message, number)
print(hidden_message)

print(caeser_decipher(hidden_message, number))