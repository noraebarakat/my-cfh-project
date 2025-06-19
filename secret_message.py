def encrypt_caesar(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            # Shift character within alphabet bounds
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char  # Non-alphabetic characters remain unchanged
    return encrypted

def decrypt_caesar(message, shift):
    return encrypt_caesar(message, -shift)

def main():
    # Encrypted version of the message
    encrypted_message = "Mjqqt! Kzs kfhy - N bts ynhpjyx yt xjj ymj Ijxuhfgqj Rj 3 Wji Hfwujy Btwqi Uwjrnjwj - Xnjwwf"
    
    # Decrypt the message with the Caesar cipher shift
    decrypted_message = decrypt_caesar(encrypted_message, 5)
    
    print("Decrypted Message:")
    print(decrypted_message)

if __name__ == '__main__':
    main()
