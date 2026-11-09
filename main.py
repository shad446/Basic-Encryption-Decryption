
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result


while True:
    print("\n" + "=" * 45)
    print("       DECODELABS | CRYPTOGRAPHY")
    print("       ENCRYPTION & DECRYPTION")
    print("=" * 45)

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nSelect an option (1-3): ")

    if choice == "1":
        message = input("\nEnter your message: ")

        try:
            shift = int(input("Enter shift key (1-25): "))

            if 1 <= shift <= 25:
                encrypted = caesar_cipher(message, shift)
                print("\nEncrypted Message:", encrypted)
            else:
                print("Shift key must be between 1 and 25.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        message = input("\nEnter encrypted message: ")

        try:
            shift = int(input("Enter original shift key (1-25): "))

            if 1 <= shift <= 25:
                decrypted = caesar_cipher(message, -shift)
                print("\nDecrypted Message:", decrypted)
            else:
                print("Shift key must be between 1 and 25.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("\nThank you for using DecodeLabs!")
        break

    else:
        print("\nInvalid option! Choose 1, 2, or 3.")
