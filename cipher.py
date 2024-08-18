def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Example usage
text = "if we do not have bagel bites than we shall trojan horse at dawn."
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)
