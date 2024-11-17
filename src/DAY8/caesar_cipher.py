import string


def main():
    def encrypt(original_text, shift) -> str:
        encrypted_text = ""
        for char in original_text:
            i = alphabet_list.index(char) + shift
            if i >= len(alphabet_list):
                i = abs(i - len(alphabet_list))

            encrypted_text += alphabet_list[i]
        return encrypted_text

    def decrypt(encrypted_text, shift) -> str:
        decrypted_text = ""
        for char in encrypted_text:
            i = alphabet_list.index(char) - shift
            if i < 0:
                i = abs(i + len(alphabet_list))
            decrypted_text += alphabet_list[i]

        return decrypted_text

    alphabet = string.ascii_lowercase
    alphabet_list = []
    for char in alphabet:
        alphabet_list.append(char)

    type = input("Type encrypt or decrypt:\n ").lower()
    if type == "encode":
        original_text = input("Type the original:")
        shift = int(input("Type number of shift: "))
        encrypt_text = encrypt(original_text, shift)
        print(encrypt_text)
    if type == "decode":
        encrypt_text = input("Type the decrypt:").lower()
        shift = int(input("Type number of shift: "))
        decrypt_text = decrypt(encrypt_text, shift)
        print(decrypt_text)



if __name__ == "__main__":
    while True:
        main()
        user_input = input("Do you want to do another encrypt or decrypt?.Type 'yes' or 'y' :").lower()
        if user_input == 'no' or user_input == 'n':
            break












